import pandas as pd 
import streamlit as st 
import os
# load the data
# # data is stored in cache memory for the faster data loading 
# load the data efficiently 
@st.cache_data
def load_data():
    """
    Load the data from the csv file
    """
    
    

    file_path = "./data/Cleaned_investment.csv"

    if os.path.exists(file_path):
       df = pd.read_csv(file_path,encoding="utf-8")
       print("File loaded successfully!")
       # add some cleaning part also 
       df['first_funding_at'] = pd.to_datetime(df['first_funding_at'], errors='coerce')

       # Extract year
       df['first_funding_year'] = df['first_funding_at'].dt.year
    
       # df['last_funding_at'] = pd.to_datetime(df['last_funding_at'], errors='coerce')
       # # extract year 
       # df['last_funding_year'] = df['last_funding_at'].dt.year
    
       # df['quarter']=df['first_funding_at'].dt.to_period('Q')
       return df
    else:
        print(f"Error: File '{file_path}' not found. Please check the path.")
    
    