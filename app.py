import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import matplotlib.pyplot as plt
import os

st.title("pandas-ai streamlit interface")

st.write("A demo interface for [PandasAI](https://github.com/Sinaptik-AI/pandas-ai)")
st.write(
    "Looking for an example *.csv-file?, check [here](https://gist.github.com/netj/8836201) (Download ZIP)."
)

if "openai_key" not in st.session_state:
    with st.form("API key"):
        key = st.text_input("OpenAI Key", value="", type="password")
        if st.form_submit_button("Submit"):
            st.session_state.openai_key = key
            st.session_state.prompt_history = []
            st.session_state.df = None
            st.success('Saved API key for this session.')

if "openai_key" in st.session_state:
    llm = OpenAI(api_key="YOUR_API_KEY")  # Update 'api_key' parameter name

    if st.session_state.df is None:
        uploaded_file = st.file_uploader(
            "Choose a CSV file. This should be in long format (one datapoint per row).",
            type="csv",
        )
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.session_state.df = SmartDataframe(st.session_state.df,config={"llm": llm})  # Use SmartDataframe to wrap the DataFrame

    with st.form("Question"):
        question = st.text_input("Question", value="", type="default")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner():
                response = st.session_state.df.ask(question)  # Use .ask() method for SmartDataframe
                if response is not None:
                    st.write(response)
                st.session_state.prompt_history.append(question)

    if st.session_state.df is not None:
        st.subheader("Current dataframe:")
        st.write(st.session_state.df.dataframe)  # Access the original DataFrame using .dataframe attribute

    st.subheader("Prompt history:")
    st.write(st.session_state.prompt_history)

if st.button("Clear"):
    st.session_state.prompt_history = []
    st.session_state.df = None
