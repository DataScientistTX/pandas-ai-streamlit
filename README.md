# pandas-ai-streamlit
A streamlit interface for pandas-ai

## Installation & Running:

```
git clone https://github.com/DataScientistTX/pandas-ai-streamlit.git
conda create --name pandasai python=3.11
conda activate pandasai
cd pandas-ai-streamlit
pip install -r requirements.txt
streamlit run app.py
```

Check requirements in case there are compatibility issues. Tested with `pandasai==2.0`.

## Streamlit Share

Running [here](https://pandas-ai-gui.streamlit.app)
Note: This is the stable version with pandas-ai version 2.0. 

## Notes
- Updated to pandasai==2.0. 
- Updated to python==3.11
- Charts are stored as `temp_chart.png` and now they are loaded from there. 
- The implementation is not perfect an might cause issues when having multiple concurrent users.

## Known issues
- Generated images are not shown

## References
- [PandasAI](https://github.com/Sinaptik-AI/pandas-ai)
- [PandasAI Streamlit](https://github.com/straussmaximilian/pandas-ai-streamlit)