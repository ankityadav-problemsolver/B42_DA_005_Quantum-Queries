import streamlit as st

# this module contain the utility functions
# that arw used in the main module 

# showing the all key metrics and kpi for the datssets
def display_metrics(df):
    """
    Display the Key Performance Indicators (KPIs)
    """
    st.subheader("📈 Key Performance Indicators")
    col1,col2,col3,col4= st.columns(4)
    with col1:
        total_funding=df['funding_total_usd'].sum()
        if total_funding > 1000000000:
            funding=f"${(total_funding/1000000000):,.3f} B"
        elif total_funding > 1000000:
            funding=f"${(total_funding/1000000):,.3f} M"
        else:
            funding=total_funding
        st.metric(label="💰 Total Funding (USD)",value=funding)
    with col2:
        st.metric(label="🚀 Number of Startups",value=df.shape[0])
    with col3:
        avg_funding=df['funding_total_usd'].mean()
        if avg_funding > 1000000000:
            funding=f"${(avg_funding/1000000000):,.3f} B"
        elif avg_funding > 1000000:
            funding=f"${(avg_funding/1000000):,.3f} M"
        else:
            funding=avg_funding
        st.metric("📊 Avg Funding per Startup",value=funding)
    with col4:
        ind_venture_fund=f"${df[df['country_code']=='IND']['venture'].sum()/1000000:,.2f}"
        st.metric(label="Total Venture Capital in India (in Million $)",value=ind_venture_fund)
    col5,col6,col7,col8=st.columns(4)
    with col5:
        st.metric(label="Total Startup Founded in India",value=df[df['country_code']=='IND']['name'].shape[0])
    with col6:
        funding_type=df.iloc[:,12:]
        most_common_funding_type=funding_type.sum().idmax()
        st.metric(label="Most Common funding Type",value=most_common_funding_type)
    with col7:
        st.metric(label="Totat Startup Founded in USA",value=df[df['country_code']=='USA']['name'].shape[0])
    with col8:
        usa_venture_fund=f"${df[df['country_code']=='USA']['venture'].sum()/1000000:,.2f}"
        st.metric(label="Total Venture Capital Funded in USA (in Millions $)",value=usa_venture_fund)
  
  
def fixed_matrix(df):
    col9,col10,col11=st.columns(3)
    with col9:
        market_ind_name = df[df['country_code']=="IND"]['market'].value_counts().idxmax()
        st.metric(label="Most Famous Market Segment in IND",value=market_ind_name)
    with col10:
        market_us_name = df[df['country_code']=="USA"]['market'].value_counts().idxmax()
        st.metric(label="Most Famous market  Segment in USA",value=market_us_name)
    with col11:
        market_us_name = df[df['country_code']=="CHN"]['market'].value_counts().idxmax()
        st.metric(label="Most Famous market  Segment in CHINA",value=market_us_name)
        
        


    