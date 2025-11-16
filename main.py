"""
GymAgent - WhatsApp Bot for Gyms
Main entry point integrating all components
"""

import os
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv

# Import bot components
from routers.intent_router import route_intent
from routers.llm_fallback import ask_llm
from utils.detect_language import LanguageDetector
from routers.flow_manager import FlowManager

# Load environment variables
load_dotenv()

# Initialize components
language_detector = LanguageDetector()

# Initialize FastAPI app
app = FastAPI(title="GymAgent WhatsApp Bot")

# Twilio webhook endpoint
@app.post("/webhook")
async def webhook(request: Request):
    """
    Handle incoming WhatsApp messages via Twilio webhook
    """
    try:
        # Get form data from Twilio
        form_data = await request.form()
        incoming_message = form_data.get("Body", "").strip()
        from_number = form_data.get("From", "")
        
        if not incoming_message:
            return PlainTextResponse("No message received")
        
        # Detect language
        lang_code = language_detector.detect(incoming_message)
        
        # Try rule-based intent routing first (with language for translation)
        reply = route_intent(incoming_message, language=lang_code)
        
        # If no rule-based match, use LLM fallback (which handles multilingual)
        if not reply:
            reply = ask_llm(incoming_message)
        
        # Create Twilio response
        response = MessagingResponse()
        response.message(reply)
        
        return PlainTextResponse(str(response), media_type="application/xml")
    
    except Exception as e:
        print(f"Error processing message: {e}")
        response = MessagingResponse()
        response.message("Sorry, I encountered an error. Please try again or contact staff.")
        return PlainTextResponse(str(response), media_type="application/xml")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "service": "GymAgent WhatsApp Bot"}


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


# For testing without WhatsApp
if __name__ == "__main__":
    import uvicorn
    
    print("Starting GymAgent WhatsApp Bot...")
    print("Webhook URL: http://localhost:8000/webhook")
    print("Health check: http://localhost:8000/health")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
