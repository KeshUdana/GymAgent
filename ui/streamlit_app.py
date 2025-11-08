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
    st.set_page_config(
        page_title="Gym Chat",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # WhatsApp-like CSS styling
    st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        
        /* WhatsApp-like background */
        .stApp {
            background: #e5ddd5 !important;
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cdefs%3E%3Cpattern id='grid' width='100' height='100' patternUnits='userSpaceOnUse'%3E%3Cpath d='M 100 0 L 0 0 0 100' fill='none' stroke='%23ffffff' stroke-width='0.5' opacity='0.1'/%3E%3C/pattern%3E%3C/defs%3E%3Crect width='100' height='100' fill='url(%23grid)'/%3E%3C/svg%3E") !important;
        }
        
        /* Main content area */
        .main .block-container {
            padding: 0;
            max-width: 100%;
        }
        
        /* WhatsApp header */
        .whatsapp-header {
            background: #075e54;
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .whatsapp-header h3 {
            margin: 0;
            font-size: 18px;
            font-weight: 500;
        }
        
        /* Message bubbles */
        .user-message {
            background: #dcf8c6 !important;
            color: #000 !important;
            padding: 8px 12px !important;
            border-radius: 7.5px !important;
            margin: 2px 0 2px auto !important;
            max-width: 75% !important;
            margin-right: 10px !important;
            word-wrap: break-word;
            box-shadow: 0 1px 0.5px rgba(0,0,0,0.13) !important;
            text-align: left;
            display: inline-block;
        }
        
        .assistant-message {
            background: #ffffff !important;
            color: #000 !important;
            padding: 8px 12px !important;
            border-radius: 7.5px !important;
            margin: 2px auto 2px 10px !important;
            max-width: 75% !important;
            word-wrap: break-word;
            box-shadow: 0 1px 0.5px rgba(0,0,0,0.13) !important;
            text-align: left;
            display: inline-block;
        }
        
        /* Chat messages container */
        .chat-messages {
            padding: 20px 10px 100px 10px;
            background: transparent;
            min-height: calc(100vh - 200px);
        }
        
        /* Chat input styling */
        .stChatInput {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #f0f0f0;
            padding: 10px;
            border-top: 1px solid #e0e0e0;
            z-index: 100;
        }
        
        .stChatInput > div {
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Override Streamlit chat message styles */
        [data-testid="stChatMessage"] {
            padding: 0 !important;
            margin: 0 !important;
            background: transparent !important;
        }
        
        [data-testid="stChatMessage"] > div {
            padding: 0 !important;
            background: transparent !important;
        }
        
        /* Hide avatars */
        [data-testid="stChatMessage"] img,
        [data-testid="stChatMessage"] svg {
            display: none !important;
        }
        
        /* Markdown content styling */
        .chat-messages .user-message p,
        .chat-messages .assistant-message p {
            margin: 0;
        }
        
        .chat-messages .user-message *,
        .chat-messages .assistant-message * {
            color: #000 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "intent_router" not in st.session_state:
        st.session_state.intent_router = IntentRouter()
    
    # WhatsApp-like header
    st.markdown("""
    <div class="whatsapp-header">
        <h3>💬 Gym Chat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat messages container
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    
    # Display chat history with WhatsApp styling
    for msg in st.session_state.chat_history:
        if msg.role == MessageRole.USER:
            # User message (right-aligned, green)
            st.markdown(
                f'<div class="user-message" style="text-align: right;"><div style="text-align: left;">{msg.content}</div></div>',
                unsafe_allow_html=True
            )
        else:
            # Assistant message (left-aligned, white)
            st.markdown(
                f'<div class="assistant-message">{msg.content}</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat input at bottom
    user_input = st.chat_input("Type a message...")
    
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

