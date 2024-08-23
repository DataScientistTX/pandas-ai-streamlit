import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_TITLE = "PandasAI Streamlit Interface"
    APP_ICON = "🐼"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DEFAULT_CSV_PATH = "data/Housing.csv"

def load_config():
    return Config()