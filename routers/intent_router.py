# intent_router.py
import re
import sys
from pathlib import Path
from typing import Optional, List

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))
from utils.json_loader import load_json
from utils.translator import translate_response

# load all static data once
try:
    _membership = load_json("data/membership.json")
    _schedule = load_json("data/schedule.json")
    _trainers = load_json("data/trainers.json")
    _faqs = load_json("data/faqs.json")
    _gym_info = load_json("data/gym_info.json")
except Exception as e:
    print(f"Error loading data files: {e}")
    _membership = {"plans": []}
    _schedule = {"today": [], "weekly": {}}
    _trainers = {"trainers": []}
    _faqs = {"faqs": []}
    _gym_info = {}

INTENT_KEYWORDS = {
    "membership": ["price", "membership", "cost", "plan", "fee", "pricing"],
    "schedule": ["schedule", "class", "classes", "timetable", "time"],
    "trainer": ["trainer", "coach", "personal trainer", "coach availability"],
    "hours": ["open", "close", "hours", "time"],
    "location": ["where", "location", "address", "how to get"],
    "parking": ["parking", "park"],
    "trial": ["trial", "free trial", "try"],
    "renew": ["renew", "renewal", "extend"],
    "faq": []  # handled separately
}

def find_intents(text: str) -> List[str]:
    t = text.lower()
    found = []
    for intent, kws in INTENT_KEYWORDS.items():
        for kw in kws:
            if kw in t:
                found.append(intent)
                break
    # also check FAQs by direct keyword presence
    for faq in _faqs.get("faqs", []):
        # check if a major word from question appears
        q = faq.get("question", "").lower()
        for w in q.split():
            if len(w) > 3 and w in t:
                found.append("faq")
                break
    return list(dict.fromkeys(found))  # deduplicate preserving order

def build_membership_reply() -> str:
    reply = "💳 *Membership Plans*\n"
    plans = _membership.get("plans", [])
    if not plans:
        return "Membership information is currently unavailable. Please contact us directly."
    for p in plans:
        name = p.get('name', 'Unknown')
        price = p.get('price', 'N/A')
        features = p.get('features', [])
        reply += f"- {name}: Rs {price} — {', '.join(features) if features else 'No features listed'}\n"
    return reply

def build_schedule_reply() -> str:
    reply = "🗓️ *Today's Classes*\n"
    today_classes = _schedule.get("today", [])
    if today_classes:
        for c in today_classes:
            class_name = c.get('class', 'Unknown')
            time = c.get('time', 'TBA')
            reply += f"- {class_name} at {time}\n"
    else:
        reply += "No classes scheduled for today.\n"
    
    # optionally append weekly highlights
    weekly = _schedule.get("weekly", {})
    if weekly:
        reply += "\nThis week's highlights:\n"
        for day, items in weekly.items():
            if items:
                reply += f"{day.title()}: {', '.join(items)}\n"
    return reply

def build_trainer_reply() -> str:
    reply = "🏋️ *Trainer Availability*\n"
    trainers = _trainers.get("trainers", [])
    if not trainers:
        return "Trainer information is currently unavailable. Please contact us directly."
    for t in trainers:
        name = t.get('name', 'Unknown')
        specialty = t.get('specialty', 'General')
        hours = t.get('hours', 'TBA')
        notes = t.get('notes', '')
        rate = t.get('rate_per_session', '')
        rate_str = f" — Rs {rate}/session" if rate else ""
        notes_str = f" — {notes}" if notes else ""
        reply += f"- {name} ({specialty}) — {hours}{rate_str}{notes_str}\n"
    return reply

def build_faq_reply(text: str) -> Optional[str]:
    # try to find best matching FAQ by simple overlap
    t = text.lower()
    best = None
    best_score = 0
    for f in _faqs.get("faqs", []):
        q = f.get("question", "").lower()
        score = sum(1 for w in q.split() if w in t and len(w) > 3)
        if score > best_score:
            best = f
            best_score = score
    if best and best_score > 0:
        return best.get("answer")
    return None

def route_intent(user_text: str, language: str = "en") -> Optional[str]:
    """
    Returns a string reply if rule-based intents cover it, else None for LLM fallback.
    If multiple intents present, combine their replies.
    
    Args:
        user_text: User's message
        language: Language code ("en", "si", "ta") for translation
    """
    intents = find_intents(user_text)
    parts = []

    if not intents:
        # try FAQ fuzzy match
        faq_reply = build_faq_reply(user_text)
        if faq_reply:
            # Translate FAQ reply if needed
            if language != "en":
                faq_reply = translate_response(faq_reply, language)
            return faq_reply
        return None

    # Build replies for detected intents in a sensible order
    for intent in intents:
        if intent == "membership":
            parts.append(build_membership_reply())
        elif intent == "schedule":
            parts.append(build_schedule_reply())
        elif intent == "trainer":
            parts.append(build_trainer_reply())
        elif intent == "hours":
            parts.append(f"Our opening hours: {_gym_info.get('opening_hours','5AM–11PM')}")
        elif intent == "location":
            location = _gym_info.get('location', 'Location information not available')
            contact = _gym_info.get('contact', 'Contact information not available')
            parts.append(f"Address: {location}\nContact: {contact}")
        elif intent == "parking":
            parts.append(_gym_info.get("parking", "No parking info available."))
        elif intent == "trial":
            parts.append("We offer a 1-day free trial. Reply 'TRIAL' to book and we'll collect your name and preferred time.")
        elif intent == "renew":
            parts.append("To renew membership, reply 'RENEW' and we'll send a secure payment link.")
        elif intent == "faq":
            faq_reply = build_faq_reply(user_text)
            if faq_reply:
                parts.append(faq_reply)

    # join parts with separators and a quick CTA
    reply = "\n\n".join(parts)
    if len(parts) > 0:
        reply += "\n\nReply 'MENU' to see options or 'HUMAN' to contact staff."
    
    # Translate reply if language is not English
    if language != "en" and reply:
        reply = translate_response(reply, language)
    
    return reply
