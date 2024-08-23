import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

def load_csv(file_path):
    return pd.read_csv(file_path)

def create_smart_dataframe(df, api_key):
    llm = OpenAI(api_key=api_key)
    return SmartDataframe(df, config={
        "llm": llm,
        "save_charts": True,
        "save_charts_path": "charts/",
        "open_charts": False
    })