import pandas as pd 
import streamlit as st 
# load the data 
@st.cache_data  # data is stored in cache memory for the faster data loading 
def load_data():
    """
    Load the data from the csv file
    """
    data=pd.read_csv("data/startup_clean_file1.csv")
    
    # add some cleaning part also 
    data['first_funding_at'] = pd.to_datetime(data['first_funding_at'], errors='coerce')

     # Extract year
    data['first_funding_year'] = data['first_funding_at'].dt.year
    
    data['last_funding_at'] = pd.to_datetime(data['last_funding_at'], errors='coerce')
    # extract year 
    data['last_funding_year'] = data['last_funding_at'].dt.year
    
    data['quarter']=data['first_funding_at'].dt.to_period('Q')
    
    if data is not None:
        return data
    else: 
        return "No data found"
    
    