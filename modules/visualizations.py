import plotly.express as px 

def plot_funding_by_market(df):
    """ 
    plot the total funding by market
    """
    total_funding=df.groupby('market')['funding_total_usd'].sum().reset_index()
    # top 10 market 
    total_funding=total_funding.sort_values(by="funding_total_usd",ascending=False).head(10)
    fig=px.bar(total_funding,x='market',y='funding_total_usd',title="Top 10 Markets by Total Funding")
    return fig

def plot_countries_by_funding(df):
    """ 
    plot the countries by funding 
    """
    countries=df.groupby('country_code')['funding_total_usd'].sum().reset_index()
    # top 10 countries by funding 
    countries=countries.sort_values(by='funding_total_usd',ascending=False).head(10)
    fig=px.bar(countries,x='country_code',y='funding_total_usd',title="Top 10 Countries by Funding")
    return fig 

def plot_funding_distribution_by_status(df):
    
    """ 
    plot the funding distribution by status 
    
    """
    funding_status_distribution=df.groupby('status')['funding_total_usd'].sum().reset_index()
    funding_status_distribution=funding_status_distribution.sort_values(by="funding_total_usd",ascending=False)
    fig=px.pie(funding_status_distribution,color="status",values="funding_total_usd",names="status",title="Funding Distribution by Status")
    return fig
       
def plot_startup_distribution_by_countries(df):
    """ 
    plot the number of startup by countries 
    """
    startup_count=df['country_code'].value_counts().reset_index().head(10)
    
    
    # top 10 countries that having the maxium number of startup
    fig=px.bar(startup_count,x='country_code',y='count',title="Number of Startup by Each Country")
    return fig

def plot_startup_by_state_of_usa(state_counts):
    """ 
    plot the number of startup by state of usa using the map of usa 
    """
    fig = px.choropleth(
        state_counts,
        locations='state_code',  # Column with state codes
        locationmode='USA-states',  # Set to plot US states
        color='startup_count',  # Column to determine color
        scope="usa",  # Limit map to USA
        title="Number of Startups by State in the USA",
        labels={'startup_count': 'Number of Startups'},
        color_continuous_scale=px.colors.sequential.Plasma
    )
    return fig