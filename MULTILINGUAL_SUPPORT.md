# Multilingual Support Documentation

## Overview

The GymAgent WhatsApp bot now **fully supports Sinhala and Tamil** in addition to English. Even though the data files (membership.json, schedule.json, etc.) are in English, all responses are automatically translated to match the user's language.

## How It Works

### 1. Language Detection
- When a user sends a message, the bot automatically detects the language
- Uses Unicode character ranges:
  - **Sinhala**: U+0D80-U+0DFF
  - **Tamil**: U+0B80-U+0BFF
  - **English**: Default fallback

### 2. Response Flow

```
User Message (Sinhala/Tamil/English)
    ↓
Language Detection
    ↓
Intent Routing (Rule-based)
    ↓
English Response from Data Files
    ↓
Translation (if not English)
    ↓
Final Response in User's Language
```

### 3. Translation Process

**Rule-Based Responses:**
- Membership plans, schedules, trainer info, FAQs, etc.
- Generated in English from JSON data files
- Automatically translated to user's language using LLM
- Formatting, emojis, and structure preserved

**LLM Fallback:**
- For complex queries not covered by rule-based intents
- LLM already configured for multilingual responses
- Responds directly in user's language

## Example Flow

### Sinhala User Asking About Membership

1. **User sends**: "සාමාජිකත්වය මිල කීයද?" (What is the membership price?)
2. **Language detected**: "si" (Sinhala)
3. **Intent detected**: "membership"
4. **English response generated**:
   ```
   💳 *Membership Plans*
   - Monthly: Rs 8500 — Gym access, Free group classes, 1 fitness assessment
   - Quarterly: Rs 24000 — Gym access, Priority booking, 2x personal training discount
   ...
   ```
5. **Translated to Sinhala**:
   ```
   💳 *සාමාජිකත්ව සැලසුම්*
   - මාසික: රු. 8500 — ව්‍යායාම ශාලාවට ප්‍රවේශය, නොමිලේ කණ්ඩායම් පන්ති, 1 ශක්තිමත්භාවය තක්සේරුව
   ...
   ```

## Implementation Details

### Files Modified

1. **`utils/translator.py`** (NEW)
   - Translation utility using OpenAI API
   - Preserves formatting and structure
   - Handles errors gracefully

2. **`routers/intent_router.py`**
   - Added `language` parameter to `route_intent()`
   - Translates responses before returning

3. **`main.py`**
   - Passes detected language to `route_intent()`

### Translation Function

```python
from utils.translator import translate_response

# Translate English text to Sinhala
sinhala_text = translate_response(english_text, "si")

# Translate English text to Tamil
tamil_text = translate_response(english_text, "ta")
```

## Benefits

✅ **Fully Multilingual**: Works in English, Sinhala, and Tamil  
✅ **No Data Duplication**: Keep data files in English only  
✅ **Automatic Translation**: No manual translation needed  
✅ **Consistent Formatting**: Preserves emojis and structure  
✅ **Fallback Support**: LLM handles complex queries in any language  

## Requirements

- `OPENAI_API_KEY` environment variable must be set
- Uses `gpt-4o-mini` model for translations
- Translation happens in real-time (adds ~1-2 seconds latency)

## Notes

- Translation only occurs for non-English languages
- If translation fails, original English text is returned
- LLM fallback already handles multilingual responses natively
- Data files remain in English for easy maintenance

