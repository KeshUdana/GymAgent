import json
from core.program_generator import generate_workout_plan
from core.mistral_client import query_mistral

def route_intent(user_input: str):
    """Route user query to appropriate logic."""
    lower = user_input.lower()

    if any(k in lower for k in ["workout", "program", "routine", "plan"]):
        return generate_workout_plan(user_input)
    elif any(k in lower for k in ["price", "membership", "cost"]):
        return get_pricing_info()
    elif any(k in lower for k in ["contact", "location", "time", "hours"]):
        return get_contact_info()
    else:
        # fallback to Mistral general query
        messages = [
            {"role": "system", "content": "You are a friendly gym assistant."},
            {"role": "user", "content": user_input},
        ]
        return query_mistral(messages)

def get_pricing_info():
    data = json.load(open("data/gym_info.json"))
    pricing = data.get("pricing", {})
    text = "\n".join([f"- {k}: {v}" for k, v in pricing.items()])
    return f"🏷️ **Pricing Info:**\n{text}"

def get_contact_info():
    data = json.load(open("data/gym_info.json"))
    contact = data.get("contact", {})
    return f"📍 Address: {data['address']}\n📞 Phone: {contact['phone']}\n⏰ Hours: {data['hours']}"
