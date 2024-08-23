import os
import streamlit as st

def save_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = api_key
    st.session_state.openai_key = api_key
    st.success('Saved API key for this session.')

def clear_session():
    st.session_state.prompt_history = []
    st.session_state.df = None
    st.success('Session cleared.')