import pandas as pd 
import streamlit as st 
# load the data 
@st.cache_data  # data is stored in cache memory for the faster data loading 
def load_data():
    """
    Load the data from the csv file
    """
    data=pd.read_csv("data/startup_clean_file1.csv")
    
    if data is not None:
        return data
    else: 
        return "No data found"
    
    