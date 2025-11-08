import streamlit as st
from core.intent_router import route_intent
from config.settings import APP_TITLE

st.set_page_config(page_title=APP_TITLE, layout="centered")

st.title(APP_TITLE)
st.caption("💬 Your personalized gym assistant powered by Mistral")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me about workouts, pricing, or memberships...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = route_intent(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
