import streamlit as st
from src.ui.components import api_key_input
from src.utils import save_api_key

def render():
    st.title("PandasAI Streamlit Interface")
    st.write("A demo interface for [PandasAI](https://github.com/Sinaptik-AI/pandas-ai)")
    
    if "openai_key" not in st.session_state:
        key = api_key_input()
        if key:
            save_api_key(key)