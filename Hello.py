import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time

# Main title
st.title("Welcome to David Sherman's website!")

# LinkedIn profile
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" 
hyperlink_url = "https://www.linkedin.com/in/david-j-sherman/"  
image_width = 50
st.markdown(
    f"""
    <div style="text-align: right;">
        <a href="{hyperlink_url}" target="_blank">
            <img src="{image_url}" alt="Clickable Image" width="{image_width}" style="float: right;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# About me section
st.divider()
st.subheader("About me:")
st.markdown("""Passionate data analyst and scientist with a robust foundation in data manipulation, 
            analysis, visualization, and interpretation. Equipped with a Master's in Data Science from UC Berkeley's School of Information, 
            I bring a dynamic skill set honed through hands-on experience. Proficient in writing SQL and Python code and adept at leveraging 
            advanced analytics tools like Tableau and PowerBI, I excel in transforming complex datasets into actionable insights. My diverse 
            background in client service and vendor management across industries, 
            such as e-commerce, consulting, and healthcare, enriches my ability to extract meaningful value from data.""")
st.divider()

col1, col2, col3, col4 = st.columns(4, gap="medium")

# Function to center subheaders
def centered_subheader(subheader_text, font_size=18):
    st.markdown(f"<h3 style='text-align: center;'>{subheader_text}</h3>", unsafe_allow_html=True)

# Create columns with details about me
with col1:
    centered_subheader("Coding Languages", font_size=12)
    st.write('''
            - SQL
            - Python
            - R
            ''')
with col2:    
    centered_subheader("Data Viz Tools", font_size=12)
    st.write('''
            - Tableau
            - Power BI
            - Looker
            - Adobe Analytics
            - ThoughtSpot
            ''')
with col3:    
    centered_subheader("Python Libraries", font_size=12)
    st.markdown("Data Processing and Modeling")
    st.write('''
            - Pandas
            - NumPy
            - SciPy
            - Keras
            - SciKit-Learn
            - PyTorch
            - TensorFlow
            - XGBoost
            ''')
    st.markdown("Data Visualization")
    st.write('''
            - Matplotlib
            - Plotly
            - Seaborn
            ''')
    st.markdown("Miscellaneous")
    st.write('''
            - Psycopg2
            - Gmaps
            - Neo4j
            - Statsmodels.api
            - Requests
            - Transformers
            - Gensim
            - NLTK
            - Re
            - SpaCy
             ''')
with col4:
    centered_subheader("Other Skills", font_size=12)
    st.write('''
            - Advanced Excel
            - Power Automate
            - API Calls
            - Middleware
            - Salesforce
            - SEM
            - SEO
             ''')

     