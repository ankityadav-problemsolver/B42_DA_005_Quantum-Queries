import streamlit as st

# Function to Inject CSS
def apply_custom_styles():
     st.markdown("""
        <style>
        .big-font { 
            font-size: 30px !important; 
            font-weight: bold; 
            color: #00c8ff; 
        }

        .medium-font { 
            font-size: 24px !important; 
            font-weight: bold; 
            color: #ffa500; 
        }

        .small-font { 
            font-size: 20px !important; 
            color: #ffffff; 
        }

        .metric-box {
            background-color: #222831; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center; 
            color: white;
            margin-top: 10px;
        }

        /* Fix Streamlit Widget Styling */
        div[data-testid="stMarkdownContainer"] {
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)
