import streamlit as st

def api_key_input():
    with st.form("API key"):
        key = st.text_input("OpenAI Key", value="", type="password")
        submitted = st.form_submit_button("Submit")
        if submitted:
            return key
    return None

def file_uploader():
    return st.file_uploader(
        "Choose a CSV file. This should be in long format (one datapoint per row).",
        type="csv"
    )

def question_input():
    with st.form("Question"):
        question = st.text_input("Question", value="", type="default")
        submitted = st.form_submit_button("Submit")
        if submitted:
            return question
    return None