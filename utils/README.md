# Utils Module

Utility functions used across the bot for common operations.

## Files

### `detect_language.py`
Language detection utility for multilingual support.

**Class: LanguageDetector**

**Methods:**
- `detect(text: str) -> str` (static method)
  - Detects language from text using Unicode ranges
  - Returns: `"en"` (English), `"si"` (Sinhala), or `"ta"` (Tamil)
  - Defaults to English if no match

**Detection Logic:**
- **Sinhala**: Unicode range U+0D80 to U+0DFF
- **Tamil**: Unicode range U+0B80 to U+0BFF
- **English**: Default fallback

**Example:**
```python
from utils.detect_language import LanguageDetector

detector = LanguageDetector()
lang = detector.detect("Hello")  # Returns "en"
lang = detector.detect("ආයුබෝවන්")  # Returns "si"
lang = detector.detect("வணக்கம்")  # Returns "ta"
```

### `json_loader.py`
Simple JSON file loading utility.

**Functions:**
- `load_json(path: str) -> dict`
  - Loads JSON file from given path
  - Path is relative to current working directory
  - Returns parsed dictionary
  - Uses UTF-8 encoding

**Example:**
```python
from utils.json_loader import load_json

data = load_json("data/membership.json")
# Returns dictionary with membership data
```

**Usage:**
- Used by `intent_router.py` to load static data files
- Handles file paths relative to project root
- Simple wrapper around `json.load()`

## Dependencies

- `json` - JSON parsing
- `os` - Path operations
- `re` - Regex for language detection

### `translator.py`
Translation utility for multilingual responses.

**Functions:**
- `translate_response(text: str, target_language: str) -> str`
  - Translates English text to target language (Sinhala/Tamil)
  - Uses OpenAI API for translation
  - Preserves formatting, emojis, and structure
  - Returns original text if translation fails or language is English
  - Requires `OPENAI_API_KEY` environment variable

**Example:**
```python
from utils.translator import translate_response

english_text = "💳 Membership Plans\n- Monthly: Rs 8500"
sinhala_text = translate_response(english_text, "si")
# Returns Sinhala translation with formatting preserved
```

## Notes

- Language detection is based on Unicode character ranges
- JSON loader uses current working directory as base
- Translator uses LLM for accurate translations
- All utilities are stateless and can be used as singletons

