import streamlit as st
from src.ui.pages import home, analysis
from src.config import load_config

def main():
    config = load_config()
    st.set_page_config(page_title=config.APP_TITLE, page_icon=config.APP_ICON)
    
    pages = {
        "Home": home.render,
        "Analysis": analysis.render
    }
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()