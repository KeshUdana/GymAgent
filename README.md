# GymAgent - WhatsApp Bot for Gyms

A multilingual WhatsApp bot designed for gyms to handle customer inquiries, membership information, schedules, trainer availability, and FAQs. Supports English, Sinhala, and Tamil languages.

## Architecture Overview

```
GymAgent/
├── main.py                 # Main entry point (to be implemented)
├── routers/                # Core routing and processing logic
│   ├── intent_router.py   # Intent detection and response generation
│   ├── flow_manager.py    # Conversation flow management
│   └── llm_fallback.py    # LLM fallback for complex queries
├── utils/                  # Utility functions
│   ├── detect_language.py # Language detection (EN/SI/TA)
│   └── json_loader.py     # JSON file loading utility
├── data/                   # Static data files
│   ├── membership.json    # Membership plans and pricing
│   ├── schedule.json      # Class schedules
│   ├── trainers.json      # Trainer information
│   ├── faqs.json          # Frequently asked questions
│   └── gym_info.json      # Gym location, hours, contact info
└── flows/                  # Conversation flows by language
    ├── en.json            # English flow definitions
    └── si.json            # Sinhala flow definitions
```

## How It Works

### 1. Message Flow
```
User Message → Language Detection → Intent Routing → Response Generation → LLM Fallback (if needed)
```

### 2. Components

#### **Intent Router** (`routers/intent_router.py`)
- Detects user intents from keywords (membership, schedule, trainer, hours, location, etc.)
- Generates structured responses from JSON data
- Handles FAQ matching with fuzzy keyword matching
- Returns `None` if no match found (triggers LLM fallback)

#### **Flow Manager** (`routers/flow_manager.py`)
- Manages conversation flows based on detected language
- Loads language-specific flow definitions from `flows/` directory
- Handles welcome messages and intent matching
- Provides fallback responses

#### **Language Detector** (`utils/detect_language.py`)
- Detects language using Unicode character ranges
- Returns: `"en"` (English), `"si"` (Sinhala), or `"ta"` (Tamil)
- Uses regex patterns for Sinhala (U+0D80-U+0DFF) and Tamil (U+0B80-U+0BFF)

#### **LLM Fallback** (`routers/llm_fallback.py`)
- Uses OpenAI API for complex queries not covered by rule-based intents
- Multilingual support (responds in user's language)
- Short, friendly, and helpful responses

### 3. Data Structure

#### Membership Data (`data/membership.json`)
- Plans: Monthly, Quarterly, Yearly, Student
- Pricing and features for each plan
- Cancellation policy

#### Schedule Data (`data/schedule.json`)
- Today's classes with times
- Weekly class highlights
- Booking information

#### Trainer Data (`data/trainers.json`)
- Trainer names, specialties, availability hours
- Rates per session
- Booking policies

#### FAQ Data (`data/faqs.json`)
- Common questions and answers
- Covers hours, classes, parking, personal training, cancellation

#### Gym Info (`data/gym_info.json`)
- Location and address
- Contact information
- Opening hours
- Parking information
- Payment methods

## Functions Reference

### `routers/intent_router.py`
- `find_intents(text: str) -> List[str]` - Finds all matching intents from user text
- `build_membership_reply() -> str` - Generates formatted membership plan response
- `build_schedule_reply() -> str` - Generates formatted schedule response
- `build_trainer_reply() -> str` - Generates formatted trainer availability response
- `build_faq_reply(text: str) -> Optional[str]` - Finds best matching FAQ answer
- `route_intent(user_text: str) -> Optional[str]` - Main routing function, returns response or None

### `routers/flow_manager.py`
- `__init__(language: str)` - Initialize with language code
- `load_flow(lang: str) -> Dict[str, Any]` - Load flow data for language
- `get_welcome() -> str` - Get welcome message for language
- `match_intent(user_message: str) -> str` - Match user message to intent patterns
- `get_response(user_message: str) -> str` - Main response handler

### `routers/llm_fallback.py`
- `ask_llm(message: str) -> str` - Sends message to OpenAI API and returns response

### `utils/detect_language.py`
- `detect(text: str) -> str` - Detects language (en/si/ta) from text

### `utils/json_loader.py`
- `load_json(path: str) -> dict` - Loads JSON file from path

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

3. Run the bot (main.py needs WhatsApp integration):
```bash
python main.py
```

## Supported Intents

- **membership**: Pricing, plans, fees
- **schedule**: Class schedules, timetables
- **trainer**: Trainer availability, personal training
- **hours**: Opening/closing times
- **location**: Address, directions
- **parking**: Parking availability
- **trial**: Free trial information
- **renew**: Membership renewal
- **faq**: General questions

## Language Support

The bot fully supports multilingual responses:

- **English (en)**: Default language
- **Sinhala (si)**: Unicode range U+0D80-U+0DFF
- **Tamil (ta)**: Unicode range U+0B80-U+0BFF

### How Multilingual Works

1. **Language Detection**: Automatically detects user's language from their message
2. **Rule-Based Responses**: English responses from data files are automatically translated to user's language using LLM
3. **LLM Fallback**: Direct multilingual responses when rule-based matching fails
4. **Translation**: Uses OpenAI API to translate structured responses (membership, schedule, trainers, etc.) while preserving formatting

**Note**: While data files are in English, all responses are automatically translated to match the user's detected language.

## Notes

- The bot uses rule-based intent matching first, then falls back to LLM for complex queries
- All data is stored in JSON files for easy updates
- Flow definitions support pattern matching for intents
- WhatsApp integration (Twilio) needs to be added to main.py

