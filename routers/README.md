# Routers Module

This module contains the core routing and processing logic for the WhatsApp gym bot.

## Files

### `intent_router.py`
Main intent detection and response generation module.

**Functions:**
- `find_intents(text: str) -> List[str]`
  - Analyzes user text and returns list of detected intents
  - Checks against keyword dictionaries and FAQ questions
  - Returns deduplicated list preserving order

- `build_membership_reply() -> str`
  - Generates formatted membership plans response
  - Includes all plans with prices and features
  - Returns markdown-formatted string

- `build_schedule_reply() -> str`
  - Generates today's class schedule
  - Includes weekly highlights
  - Returns formatted string with emojis

- `build_trainer_reply() -> str`
  - Generates trainer availability information
  - Includes names, specialties, hours, and rates
  - Returns formatted string

- `build_faq_reply(text: str) -> Optional[str]`
  - Fuzzy matches user text against FAQ questions
  - Uses word overlap scoring
  - Returns best matching answer or None

- `route_intent(user_text: str) -> Optional[str]`
  - Main routing function
  - Detects intents and builds combined response
  - Returns formatted reply string or None (for LLM fallback)
  - Handles multiple intents in one message

**Data Sources:**
- Loads from `data/membership.json`
- Loads from `data/schedule.json`
- Loads from `data/trainers.json`
- Loads from `data/faqs.json`
- Loads from `data/gym_info.json`

**Intent Keywords:**
- membership: price, membership, cost, plan, fee, pricing
- schedule: schedule, class, classes, timetable, time
- trainer: trainer, coach, personal trainer, coach availability
- hours: open, close, hours, time
- location: where, location, address, how to get
- parking: parking, park
- trial: trial, free trial, try
- renew: renew, renewal, extend
- faq: handled via fuzzy matching

### `flow_manager.py`
Manages conversation flows based on language.

**Class: FlowManager**

**Methods:**
- `__init__(language: str)`
  - Initializes with language code (en/si/ta)
  - Loads flow data for specified language

- `load_flow(lang: str) -> Dict[str, Any]`
  - Loads flow JSON file from `flows/` directory
  - Falls back to default.json if language file not found
  - Returns flow data dictionary

- `get_welcome() -> str`
  - Returns welcome message for current language

- `match_intent(user_message: str) -> str`
  - Matches user message against intent patterns in flow data
  - Uses regex pattern matching
  - Returns response string or fallback message

- `get_response(user_message: str) -> str`
  - Main response handler
  - Checks for greeting messages (hi, hello, hey)
  - Returns welcome or matched intent response

**Flow Structure:**
```json
{
  "welcome": "Welcome message...",
  "intents": {
    "intent_name": {
      "patterns": ["pattern1", "pattern2"],
      "response": "Response text"
    }
  }
}
```

### `llm_fallback.py`
Handles LLM fallback for complex queries.

**Functions:**
- `ask_llm(message: str) -> str`
  - Sends message to OpenAI API
  - Uses model: `gpt-4.1-mini`
  - System prompt: Multilingual gym assistant
  - Returns response content
  - Requires `OPENAI_API_KEY` environment variable

**API Configuration:**
- Endpoint: `https://api.openai.com/v1/chat/completions`
- Model: `gpt-4.1-mini`
- System role: Multilingual gym assistant (FitFlow AI)
- Response style: Short, friendly, helpful

## Usage Flow

1. User sends message via WhatsApp
2. `intent_router.route_intent()` attempts rule-based matching
3. If match found, returns formatted response
4. If no match, `llm_fallback.ask_llm()` handles query
5. `flow_manager` can be used for structured conversation flows

## Dependencies

- `json` - JSON parsing
- `re` - Regex pattern matching
- `pathlib` - Path handling
- `typing` - Type hints
- `os` - Environment variables
- `requests` - HTTP requests to OpenAI API
- `utils.json_loader` - JSON file loading

