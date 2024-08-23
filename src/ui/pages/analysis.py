import streamlit as st
from src.ui.components import file_uploader, question_input
from src.data_loader import load_csv, create_smart_dataframe
from src.analysis import analyze_data
from src.config import load_config

def render():
    config = load_config()
    
    if "df" not in st.session_state:
        uploaded_file = file_uploader()
        if uploaded_file:
            df = load_csv(uploaded_file)
            st.session_state.df = df
            st.session_state.smart_df = create_smart_dataframe(df, config.OPENAI_API_KEY)
    
    if "df" in st.session_state:
        question = question_input()
        if question:
            with st.spinner():
                response = analyze_data(st.session_state.smart_df, question)
                st.write(response)
                st.session_state.prompt_history.append(question)
        
        st.subheader("Current dataframe:")
        st.write(st.session_state.df)
        
        st.subheader("Prompt history:")
        st.write(st.session_state.prompt_history)