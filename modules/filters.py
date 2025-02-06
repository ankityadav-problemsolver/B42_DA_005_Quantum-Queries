import streamlit as st 
import pandas as pd 

def filter_data(title,option_list):
    selected=st.sidebar.multiselect(title,option_list)
    selected_all=st.sidebar.checkbox("Select All",value=True,key=title)
    if selected_all:
        selected_options=option_list
    else:
        selected_options=selected
    return selected_options