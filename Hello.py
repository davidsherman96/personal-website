import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time


st.title("Welcome to David Sherman's personal website!")
st.divider()
st.subheader("About me:")
st.markdown("""Passionate data analyst and scientist with a robust foundation in data manipulation, 
            analysis, visualization, and interpretation. Equipped with a Master's in Data Science from UC Berkeley's School of Information, 
            I bring a dynamic skill set honed through hands-on experience. Proficient in writing SQL and Python code and adept at leveraging 
            advanced analytics tools like Tableau and PowerBI, I excel in transforming complex datasets into actionable insights. My diverse 
            background in client service and vendor management across industries, 
            such as e-commerce, consulting, and healthcare, enriches my ability to extract meaningful value from data.""")
st.divider()

col1, col2, col3 = st.columns(3, gap="medium")

# Function to center subheaders
def centered_subheader(subheader_text):
    st.markdown(f"<h3 style='text-align: center;'>{subheader_text}</h3>", unsafe_allow_html=True)

with col1:
    centered_subheader("Coding Languages")
    st.write('''
            - SQL (SQL Server, PostgreSQL, Redshift, Snowflake)
            - Python
            - R
            ''')
with col2:    
    centered_subheader("Data Visualization Applications")
    st.write('''
            - Tableau
            - Power BI
            - Looker
            - Adobe Analytics
            - ThoughtSpot
            ''')
with col3:    
    centered_subheader("Python Libraries")
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
    with st.expander("Miscellaneous"):
        #st.markdown("Miscellaneous")
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