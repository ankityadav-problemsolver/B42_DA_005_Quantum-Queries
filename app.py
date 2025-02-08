import streamlit as st  # type: ignore
import pandas as pd # type: ignore
from modules.lottie_animation import load_lottie_url
from streamlit_lottie import st_lottie
from modules.data_loader import load_data
from modules.filters import filter_data
from modules.modrendesign_kpi import modern_metrics
from modules.visualizations import (plot_3d_heatmaps_in_funding_rounds,
    plot_bubble_funding_growth_per_years, plot_countries_by_funding, plot_funding_by_market,
    plot_funding_distribution_by_status, plot_startup_by_state_of_usa,
    plot_startup_distribution_by_countries, plot_total_global_funding_by_country,
    plot_yearly_funding_trends)
from modules.data_usa_load import load_usa_data 

# call the animation function 
lottie_animation=load_lottie_url("assets/footer_animation.json")

# set the page for the dashboard 
st.set_page_config(page_title="Startup Dashboard",layout="wide",page_icon=":chart_with_upwards_trend:")

# load the data

df=load_data() 
# title of the dashboard
# custom style for title 

# Inject CSS to Style st.title()
st.markdown("""
    <style>
    /* Custom Style for st.title() */
    div[data-testid="stAppViewContainer"] h1 {
        color: #00c8ff !important;  /* Bright Cyan */
        font-size: 42px !important;
        font-weight: bold !important;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 200, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Use st.title()

st.title("📊 Startup Investment Analytics Dashboard")


# Sidebar Title with Custom Styling
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        color: #FF8518;  /* Vibrant Orange */
        text-align: center; 
        font-size: 26px;
        font-weight: bold;
        padding: 10px 5px;
        border-radius: 8px;
        background: linear-gradient(90deg, #FF8518, #FF5733);
        box-shadow: 2px 2px 5px rgba(255, 133, 24, 0.5);
        border: 2px solid #ffffff;
        margin-bottom: 20px; /* Adds space below the title */
    }
    </style>
    <h2 class="sidebar-title">🏆 Quantum Queries</h2>
    """, unsafe_allow_html=True)
# on side bar add the logo of the project 
st.sidebar.markdown("""
    <style>
    .sidebar-logo {
        display: block;
        margin: 5px auto;  /* Adds space above and centers the logo */
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
st.sidebar.image("assets/logo.webp", width=160)
st.sidebar.markdown('</div>', unsafe_allow_html=True)




# filter option for the dashboard 
st.sidebar.title("Filters")
selected_country=filter_data("Select Country",df['region'].unique())
selected_market=filter_data("Select Market or Category",df['market'].unique())
selected_country_codes=filter_data("Select Country Code",df['country_code'].unique())
selected_state_codes=filter_data("Select State Data",df['state_code'].unique())
filtered_data=df[(df['market'].isin(selected_market)) & (df['region'].isin(selected_country)) & (df['state_code'].isin(selected_state_codes)) & (df['country_code'].isin(selected_country_codes))]


#key metrics for the dashboard
modern_metrics(filtered_data) 

st.markdown("---")


# data visualizations 
col1,col2=st.columns(2)
with col1:
     # Section for Charts
    st.markdown("<h2 class='medium-font'>📊 Total Funding By Market</h2>", unsafe_allow_html=True)
    st.plotly_chart(plot_funding_by_market(filtered_data),use_container_width=True)
    st.markdown("📊 Summary : The Total Funding by Market analysis highlights the distribution of funding across different industries, helping investors identify high-growth sectors and market trends.")
with col2:
    # Country by Funding
    st.markdown("<h2 class='medium-font'>📊 Country by Funding</h2>", unsafe_allow_html=True)
    st.plotly_chart(plot_countries_by_funding(filtered_data),use_container_width=True)
    st.markdown("📊 Summary: The Funding by Country Code analysis provides insights into how investment is distributed across different countries, helping investors identify key markets and emerging opportunities.")
    
st.markdown("---")
col3,col4=st.columns(2)
with col3:
    # Funding Distribution by Status
    st.markdown("<h2 class='medium-font'>📊 Funding Distribution by Status</h2>", unsafe_allow_html=True)
    st.plotly_chart(plot_funding_distribution_by_status(filtered_data),use_container_width=True)
    st.markdown("📊 Summary:The Funding Distribution by Startup Status analysis categorizes funding based on a startup's current status—Operating, Closed, or Acquired. This helps investors understand how capital flows across active, failed, and merged startups, providing insights into market stability and investment risks.")
    
with col4:
    st.markdown("<h2 class='medium-font'>📊 Top 10 Countries that  Large Number of Startup</h2>", unsafe_allow_html=True)
    st.plotly_chart(plot_startup_distribution_by_countries(filtered_data),use_container_width=True)
    st.markdown("📊 Summary:The Number of Startups by Country Code analysis showcases the distribution of startups across different countries, helping investors and analysts identify regions with high entrepreneurial activity and emerging startup ecosystems.")
st.markdown("---")


# Advanced Visualizations 


# Number of Startups by State in the USA
state_count=load_usa_data(df)
st.markdown("<h2 class='medium-font'>📊 Number of Startups by State in the USA</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_startup_by_state_of_usa(state_count),use_container_width=True)
st.markdown("📊 Summary:The Number of Startups by U.S. State analysis highlights the distribution of startups across different states in the U.S., helping investors and policymakers identify key startup hubs and emerging innovation centers")

st.markdown("---")

# 3D Correelation Heatmap by Funding Rounds
st.markdown("<h2 class='medium-font'>📊 3D Correlation Heatmap by Funding Rounds</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_3d_heatmaps_in_funding_rounds(filtered_data),use_container_width=True)
st.markdown(" Summary : 📊 3D Funding Correlation Heatmap – A 3D heatmap revealing relationships between different startup funding rounds, helping investors understand funding trends.")

st.markdown("---")

# Total Funding by Country
st.markdown("<h2 class='medium-font'>📊 Total Funding by Country</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_total_global_funding_by_country(filtered_data),use_container_width=True)
st.markdown("📊 Summary:The Total Funding by Country analysis provides insights into the overall investment received by startups in different countries, helping investors identify leading markets and assess global funding trends.")

st.markdown("---")

# Yearly Funding Trends 

st.markdown("<h2 class='medium-font'>📊 Yearly Funding Trends</h2>", unsafe_allow_html=True)
start_year, end_year = st.slider("Select Year Range for line", 
                                 min_value=df["first_funding_year"].min(), 
                                 max_value=df["first_funding_year"].max(), 
                                 value=(df["first_funding_year"].min(), df["first_funding_year"].max()))
year_filtered_data_line_chart = df[(df["first_funding_year"] >= start_year) & (df["first_funding_year"] <= end_year)]

st.plotly_chart(plot_yearly_funding_trends(year_filtered_data_line_chart),use_container_width=True)
st.markdown("📊 Summary:This analysis tracks funding patterns over the years, helping investors identify growth trends, market fluctuations, and emerging investment opportunities.")

st.markdown("---")

# funding growth per year 
st.markdown("<h2 class='medium-font'>📊 Funding Growth by Years</h2>", unsafe_allow_html=True)
start_year, end_year = st.slider("Select Year Range for Growth", 
                                 min_value=df["first_funding_year"].min(), 
                                 max_value=df["first_funding_year"].max(), 
                                 value=(df["first_funding_year"].min(), df["first_funding_year"].max()))
year_filtered_data = df[(df["first_funding_year"] >= start_year) & (df["first_funding_year"] <= end_year)]

st.plotly_chart(plot_bubble_funding_growth_per_years(year_filtered_data),use_container_width=True) 
st.markdown("📊 Summary:This analysis highlights the yearly funding growth, showcasing trends in investment increases, market expansion, and sector-wise funding shifts over time.")


# footer section of my Dashboard 

st.markdown("---")
col5,col6=st.columns([1.5,2])
with col5:
    st.markdown("<h3 class='medium-font'>About the Project</h3>",unsafe_allow_html=True)
    st.markdown("""
                
                This **Startup Investments Analysis Dashboard** provides insights into startup funding trends, 
            market distribution, and more. The project aims to help investors and entrepreneurs make 
            data-driven decisions.           
                """)

    st.markdown("<h3 class='medium-font'>Team Members</h3>",unsafe_allow_html=True)
    
    st.markdown("""
                "I sincerely appreciate everyone's dedication, teamwork, and hard work in making this project a success. It was a pleasure leading such a motivated team and seeing our collective efforts come to life. Looking forward to more collaborations and achievements together!" 🚀👏
                - **Ankit**
                - **Sadnya Kolhe**
                - **Vishal Kapoor**
                - **Sarika**
                """)

# second columns we have the animated image 
with col6:
     if lottie_animation:
        st_lottie(lottie_animation,height=600,width=600,key="footer_animation")
     else:
        st.error("Failed to load the Lottie animation. Check the file path.")

# custom css for the footer section
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #262730;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>

    <div class="footer">
        <p>© 2025 Startup Investments Dashboard | <b>Team : Quantum Queries </b></p>
    </div>
    """, unsafe_allow_html=True)