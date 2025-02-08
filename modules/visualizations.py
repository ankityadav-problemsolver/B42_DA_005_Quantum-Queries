import plotly.express as px 
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def plot_funding_by_market(df):
    """ 
    plot the total funding by market
    """
    total_funding=df.groupby('market')['funding_total_usd'].sum().reset_index()
    # top 10 market 
    total_funding=total_funding.sort_values(by="funding_total_usd",ascending=False).head(10)
    # for 3d graph we use the graph objects in plotly 
    fig=go.Figure()
    
    fig.add_trace(go.Bar(
        x=total_funding['market'],
        y=total_funding['funding_total_usd'],
        text=total_funding['funding_total_usd'],
        textposition="auto",
        marker=dict(color=total_funding['funding_total_usd'],colorscale='aggrnyl',showscale=True),
        opacity=0.89
    )
    )
    
    # update layout 
    fig.update_layout(
        title="Top 10 Markets by Total Funding",
        xaxis=dict(title="Market",tickangle=45),
        yaxis=dict(title="Total Funding(USD)"),
        bargap=0.15,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)", 
    )
    # fig=px.bar(total_funding,x='market',y='funding_total_usd',title="Top 10 Markets by Total Funding",color_discrete_sequence=['#90EE90'])
    return fig

def plot_countries_by_funding(df):
    """ 
    plot the countries by funding 
    """
    countries=df.groupby('country_code')['funding_total_usd'].sum().reset_index()
    # top 10 countries by funding 
    countries=countries.sort_values(by='funding_total_usd',ascending=False).head(10)
    fig=go.Figure()
    fig.add_trace(go.Bar(
        x=countries['country_code'],
        y=countries['funding_total_usd'],
        text=countries['funding_total_usd'],
        textposition="auto",
        orientation='v',
        marker=dict(
            color=countries['funding_total_usd'],
            colorscale="plotly3",
            showscale=True,
        ),
        opacity=0.85
    ))
    
    # update layout for better visualizations
    fig.update_layout(
        title="Top 10 Countries by Total Funding",
        xaxis=dict(title='Country Code',tickangle=0),
        yaxis=dict(title="Total Funding (USD)"),
        bargap=0.2,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    ) 
    # fig=px.bar(countries,x='country_code',y='funding_total_usd',title="Top 10 Countries by Funding")
    return fig 

def plot_funding_distribution_by_status(df):
    
    """ 
    plot the funding distribution by status 
    
    """
    funding_status_distribution=df.groupby('status')['funding_total_usd'].sum().reset_index()
    funding_status_distribution=funding_status_distribution.sort_values(by="funding_total_usd",ascending=False)
    fig=px.pie(funding_status_distribution,
               color="status",
               values="funding_total_usd",
               names="status",title="Funding Distribution by Status",
               hole=0.6
               )
    fig.update_traces(
    textinfo="label+percent",  # Show both category name & percentage
    textposition="outside",  # Position labels outside with leader lines
    pull=[0.05, 0, 0, 0]  # Slightly pull out the first slice for emphasis
)
    return fig
       
def plot_startup_distribution_by_countries(df):
    """ 
    plot the number of startup by countries 
    """
    startup_count=df['country_code'].value_counts().reset_index().head(10)
    
    
    # top 10 countries that having the maxium number of startup
    fig=px.bar(startup_count,y='country_code',x='count',title="Number of Startup by Each Country",color_discrete_sequence=['#90EE90'])
    return fig

def plot_startup_by_state_of_usa(state_counts):
    """ 
    plot the number of startup by state of usa using the map of usa 
    """
    fig = px.choropleth(
        state_counts,
        locations='state_code',  #   # Column in 'state_counts' that contains state codes (like 'CA' for California, 'TX' for Texas)
        locationmode='USA-states',  # Tells Plotly to map based on USA state codes
        color='startup_count',  # Column to determine color
        scope="usa",  # Limit map to USA
        title="Number of Startups by State in the USA",
        labels={'startup_count': 'Number of Startups'},
        color_continuous_scale=px.colors.sequential.Plasma   # Defines the color scale (darker colors = more startups)

    )
    return fig

def plot_3d_heatmaps_in_funding_rounds(df):
    funding_columns=['seed','venture','angel','round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H','funding_total_usd']
    df_funding=df[funding_columns]
    # find the value of correlation cofficient values 
    corr_matrix=df_funding.corr()
    columns=corr_matrix.columns
    values=corr_matrix.values
    
    # create the pyramid structure for the visulizations 
    x,y=np.meshgrid(np.arange(len(columns)),np.arange(len(columns)))
    z=np.triu(values) # keep only values in the triangngular shapes 
    
    fig=go.Figure() # create a surface 
    fig.add_trace(go.Surface(z=z,x= columns,y= columns,colorscale="viridis",opacity=0.9))
    
    # update the layout for better visualizations 
    fig.update_layout(
        title="3D Correlation Heatmap of  Different Funding Round",
        scene=dict(
            xaxis_title="Seed Funding",
            yaxis_title="Venture Funding",
            zaxis_title="Correlation Cofficient Values",
            camera=dict(eye=dict(x=2.5,y=2.5,z=1.5)) ,# adjust the camera angle for better visualizations
            xaxis=dict(tickfont=dict(size=14)),
            yaxis=dict(tickfont=dict(size=14))
        ),
        autosize=False,
        width=600,
        height=1200,
        margin=dict(l=20,r=20,b=20,t=50)
    )
    return fig

def plot_total_global_funding_by_country(df):
    """ 
    global funding by country in the world map 
    """
    
    funding_by_country=df.groupby('country_code')['funding_total_usd'].sum().reset_index()
    fig=px.choropleth(funding_by_country,
                  locations='country_code',
                  title="Total Funding by Country",
                  color="funding_total_usd",
                  hover_name="country_code",
                  color_continuous_scale="viridis",
                  labels={'finding_total_usd': "Total Funding (USD)"}
                )
    # customize the layout for better and interactive visuliazations  and make the global map clear 
    fig.update_geos(
        showcoastlines=True,
        coastlinecolor="black",
        projection_type="natural earth",
        projection_scale=1.2, # make the global more appealing 
        
    )
    
    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="lightgrey",
            showlakes=True,
            lakecolor="lightblue"
        ),
        # title=dict(x=0.5), # place the title at center 
        height=500, #  adjust height to make the global map larger
        margin=dict(r=0,l=0,b=0,t=50) # margin for the graph for the better visulizations 
        
    )
    return fig

def plot_yearly_funding_trends(df):
    """
    yearly funding trends  
    """
    
    # yearly funding trends 
    funding_yearly=df.groupby('first_funding_year')['funding_total_usd'].sum().reset_index()
    
    # recent funding year 
    last_funding_year=df['first_funding_year'].max()
    # funding values or amount 
    last_funding_amount=funding_yearly[funding_yearly['first_funding_year']==last_funding_year]['funding_total_usd'].values[0]
    
    # draw the line chart 

    fig=px.line(funding_yearly,x='first_funding_year',y='funding_total_usd',
                title="Yearly Total Funding Raised",markers=True,
                )
    
    # adding the annotation for last_funding year and last_funding amount 
    fig.add_annotation(
        x=last_funding_year,
        y=last_funding_amount,
        text=f"Last Funding Year :{last_funding_year}",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        borderpad=5,
        bordercolor="Black",
        bgcolor="#FFD700",
        font=dict(size=12,color="black")
    )
    
    
    # update the layout and background color 
    fig.update_layout(
        plot_bgcolor="#1E1E1E",  # Dark Grey Background
        paper_bgcolor="#1E1E1E",
        font=dict(color="white"),
        xaxis=dict(
            showgrid=True, # add horizontal grid lines
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True, # add vertical gridlines
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=False
        ),
        title=dict(x=0.5),
        margin=dict(l=40,r=40,t=40,b=40), # add margin
        
    )
    return fig

def plot_bubble_funding_growth_per_years(df):
    """ 
    bubble plot funding growth over years 
    """
    df['market']=df['market'].fillna("Unknown")
    fig=px.scatter(
        df,
        x="first_funding_year",
        y='funding_total_usd',
        size="funding_total_usd",
        color='market', # market is categorial data 
        hover_name='market',
        size_max=80,
        title="Funding Growth over Time (Bubble Chart)",
        color_continuous_scale="viridis", # enhanced color visualix=zation
        labels={'first_funding_year': "Year",'funding_total_usd':'Total Funding (USD)'},
        hover_data=['first_funding_year','funding_total_usd'],# getting the deeper insights from the data when hover on it 
    )
    
    # update the layout and add some custom interative 
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title='Total Funding(USD)',
        title="Funding Growth over Time",
        showlegend=True, # show legend
        plot_bgcolor="#1E1E1E",  # Dark Grey Background
        paper_bgcolor="#1E1E1E", # black background for better visability
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        margin=dict(l=40,r=40,t=40,b=40),
        hovermode="closest",
        dragmode="zoom"
        
    )
     
    return fig
    