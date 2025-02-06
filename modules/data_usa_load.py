import streamlit as st
# take out the all the data and from that data we find the usa data 
# load the usa load 
@st.cache_data
def load_usa_data(df):
    usa_df=df[df['country_code']=='USA']
    # find the number od startup in each state of the usa
    state_counts=usa_df['state_code'].value_counts().reset_index()
    state_counts.columns=['state_code','startup_count']
    return state_counts