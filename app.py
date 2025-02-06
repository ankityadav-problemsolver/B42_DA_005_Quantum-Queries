import streamlit as st 
import pandas as pd
from modules.data_loader import load_data
from modules.utils import display_metrics
from modules.filters import filter_data
from modules.visualizations import (plot_countries_by_funding, plot_funding_by_market,
    plot_funding_distribution_by_status, plot_startup_by_state_of_usa,
    plot_startup_distribution_by_countries)
from modules.data_usa_load import load_usa_data
# set the page for the dashboard 
st.set_page_config(page_title="Startup Dashboard",layout="wide",page_icon=":chart_with_upwards_trend:")

# load the data

df=load_data() 
# title of the dashboard
st.title("📊 Data Investment Analytics Dashboard")
st.sidebar.title("🏆 Quantum Queries")
# on side bar add the logo of the project 
st.sidebar.image("assets/quantum_queries_logo.png",width=120)

# filter option for the dashboard 

selected_country=filter_data("Select Country",df['region'].unique())
selected_market=filter_data("Select Market or Category",df['market'].unique())
filtered_data=df[(df['market'].isin(selected_market)) & (df['region'].isin(selected_country))]
#key metrics for the dashboard
display_metrics(filtered_data)

# data visualizations 

col1,col2=st.columns(2)
with col1:
    st.subheader("Total Funding By Market")
    st.plotly_chart(plot_funding_by_market(filtered_data),use_container_width=True)
with col2:
    st.subheader("Country by Funding")
    st.plotly_chart(plot_countries_by_funding(filtered_data),use_container_width=True)
    
col3,col4=st.columns(2)
with col3:
    st.subheader("Funding Distribution by Status")
    st.plotly_chart(plot_funding_distribution_by_status(filtered_data),use_container_width=True)
with col4:
    st.subheader("Top 10 Countries that  Large Number of Startup")
    st.plotly_chart(plot_startup_distribution_by_countries(filtered_data),use_container_width=True)
    
state_count=load_usa_data(df)



st.subheader("Number of Startups by State in the USA")
st.plotly_chart(plot_startup_by_state_of_usa(state_count),use_container_width=True)