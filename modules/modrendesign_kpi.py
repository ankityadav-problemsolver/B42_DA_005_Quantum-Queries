import streamlit as st

def modern_metrics(df):
    
    # compute all kpi data dynamically 
    total_funding=df['funding_total_usd'].sum()/1e9 #convert into billions
    total_startups=df.shape[0]
    avg_funding=df['funding_total_usd'].mean()/1e6 # convert into millions
    total_startup_in_india=df[df['country_code']=='IND']['name'].shape[0]
    venture_amount_in_india=df[df['country_code']=='IND']['venture'].sum() / 1e6 # convert into millions
    venture_amount_in_USA=df[df['country_code']=='USA']['venture'].sum() / 1e6 # convert into millions
    funding_type=df.iloc[:,12:]
    # most_common_funding_type=df[funding_type].mode()[0]
    # Custom Styling
    st.markdown("""
        <style>
        .big-font { font-size:30px !important; font-weight: bold; color: #00c8ff; }
        .medium-font { font-size:24px !important; font-weight: bold; color: #ffa500; }
        .small-font { font-size:20px !important; color: #ffffff; }
        .metric-box {
            background-color: #222831; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center; 
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='big-font'>📊 Data Investment Analytics Dashboard</h1>", unsafe_allow_html=True)

    # Key Performance Indicators Section
    st.markdown("<h2 class='medium-font'>📌 Key Performance Indicators</h2>", unsafe_allow_html=True)

    # Create a Layout with Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<div class='metric-box'>💰 <b>Total Funding (USD)</b><br><span class='small-font'>${total_funding:.3f} B</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>📈 <b>Total Startups</b><br><span class='small-font'>{total_startups}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>🚀 <b>Most Common Funding Type</b><br><span class='small-font'>Venture</span></div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div class='metric-box'>📊 <b>Avg Funding per Startup</b><br><span class='small-font'>${avg_funding:.3f} M</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>🏢 <b>Total Startups Founded in India</b><br><span class='small-font'>{total_startup_in_india}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>🛒 <b>Most Famous Market Segment in India</b><br><span class='small-font'>E-Commerce</span></div>", unsafe_allow_html=True)

    with col3:
        st.markdown(f"<div class='metric-box'>💵 <b>Total Venture Capital in India (M$)</b><br><span class='small-font'>${venture_amount_in_india:.2f} M</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>🌎 <b>Total Venture Capital Funded in USA</b><br><span class='small-font'>${venture_amount_in_USA:.2f} M </span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>🧬 <b>Most Famous Market Segment in USA</b><br><span class='small-font'>Biotechnology</span></div>", unsafe_allow_html=True)

   
