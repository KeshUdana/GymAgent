"""Streamlit UI application."""

import streamlit as st
from handlers.intent_router import IntentRouter
from config.settings import get_settings
from models.chat import ChatMessage, MessageRole
from utils.logging import setup_logging


def create_app() -> None:
    """Create and configure the Streamlit app."""
    # Set up logging
    setup_logging()
    
    # Get settings
    settings = get_settings()
    
    # Configure page
    st.set_page_config(page_title=settings.APP_TITLE, layout="centered")
    
    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "intent_router" not in st.session_state:
        st.session_state.intent_router = IntentRouter()
    
    # App header
    st.title(settings.APP_TITLE)
    st.caption(settings.APP_DESCRIPTION)
    
    # Chat input
    user_input = st.chat_input("Ask me about workouts, pricing, or memberships...")
    
    # Handle user input
    if user_input:
        # Add user message to history
        user_message = ChatMessage(role=MessageRole.USER, content=user_input)
        st.session_state.chat_history.append(user_message)
        
        # Get response from router
        router = st.session_state.intent_router
        response_content = router.route(user_input)
        
        # Add assistant response to history
        assistant_message = ChatMessage(role=MessageRole.ASSISTANT, content=response_content)
        st.session_state.chat_history.append(assistant_message)
        
        # Rerun to update UI
        st.rerun()
    
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg.role.value):
            st.markdown(msg.content)

