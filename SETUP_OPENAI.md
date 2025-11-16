# OpenAI GPT API Setup Guide

This guide will help you set up the OpenAI GPT API for your GymAgent chatbot.

## Quick Setup

### Step 1: Get Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the API key (it starts with `sk-`)

**Important**: Save the key immediately - you won't be able to see it again!

### Step 2: Add API Key to .env File

1. Open your `.env` file in the project root directory
2. Add or update the following line:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Replace `sk-your-actual-api-key-here` with your actual API key from Step 1.**

### Step 3: Verify Setup

The chatbot uses OpenAI API in two places:
- **LLM Fallback** (`routers/llm_fallback.py`): Handles complex queries that don't match rule-based intents
- **Translation** (`utils/translator.py`): Translates responses to Sinhala/Tamil

Both will automatically use the `OPENAI_API_KEY` from your `.env` file.

### Step 4: Test the Setup

Run your chatbot:

```bash
python main.py
```

The chatbot will automatically load the `.env` file using `python-dotenv`.

## Current Configuration

- **Model**: `gpt-4o-mini` (cost-effective, fast)
- **Endpoint**: `https://api.openai.com/v1/chat/completions`
- **Usage**: 
  - LLM fallback for unanswered queries
  - Translation of structured responses (membership, schedule, trainers)

## Troubleshooting

### "AI service is not configured" Error

This means `OPENAI_API_KEY` is not set or not loaded. Check:
1. `.env` file exists in the project root
2. `.env` file contains `OPENAI_API_KEY=sk-...`
3. No extra spaces around the `=` sign
4. The API key is valid and active

### API Errors

If you see API errors:
1. Verify your API key is correct
2. Check your OpenAI account has credits/billing set up
3. Ensure you have access to `gpt-4o-mini` model
4. Check your internet connection

### Testing API Key

You can test your API key manually:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"Key starts with: {api_key[:7]}...")
```

## Security Notes

⚠️ **Important Security Tips:**

1. **Never commit `.env` to Git** - It should be in `.gitignore`
2. **Keep your API key secret** - Don't share it publicly
3. **Rotate keys regularly** - If exposed, regenerate immediately
4. **Monitor usage** - Check OpenAI dashboard for unexpected usage

## Example .env File

Your `.env` file should look like this:

```env
OPENAI_API_KEY=sk-proj-abc123xyz789...
```

That's it! Just one line with your API key.

## Need Help?

- OpenAI API Docs: https://platform.openai.com/docs
- OpenAI Support: https://help.openai.com

