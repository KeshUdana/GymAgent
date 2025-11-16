# Flows Module

Language-specific conversation flow definitions for structured bot interactions.

## Files

### `en.json`
English conversation flow definitions.

**Structure:**
```json
{
  "welcome": "Welcome message text",
  "intents": {
    "intent_name": {
      "patterns": ["pattern1", "pattern2"],
      "response": "Response text"
    }
  }
}
```

**Intents:**
- `pricing`: Price, cost, membership, fees
- `hours`: Open, close, time, hours
- `personal_training`: Trainer, coaching, personal training

**Used by:** `routers/flow_manager.py` for English conversations

### `si.json`
Sinhala conversation flow definitions.

**Structure:**
Same as `en.json` but with Sinhala text and Unicode characters.

**Intents:**
- `මිලකරණය` (pricing): මිල, පිරිවැය, සාමාජිකත්වය, ගාස්තු
- `පැය` (hours): විවෘත, වසා ඇත, කාලය, පැය
- `personal_training`: පුහුණුකරු, පුහුණු කිරීම, පුද්ගලික පුහුණුව

**Used by:** `routers/flow_manager.py` for Sinhala conversations

## Flow Manager Integration

The `FlowManager` class loads these files based on detected language:

1. User message received
2. Language detected (en/si/ta)
3. Flow file loaded: `flows/{lang}.json`
4. Patterns matched against user message
5. Response returned from matched intent

## Pattern Matching

- Uses regex pattern matching (case-insensitive)
- Patterns are simple keywords/phrases
- First match wins
- Fallback message if no match

## Adding New Languages

To add a new language (e.g., Tamil):

1. Create `flows/ta.json`
2. Copy structure from `en.json`
3. Translate welcome message and responses
4. Update `flow_manager.py` if needed
5. Ensure language detection supports the language

## Notes

- File encoding: UTF-8 (required for Sinhala/Tamil)
- Patterns are case-insensitive
- Flow manager falls back to `default.json` if language file not found
- Currently only English and Sinhala flows are implemented

