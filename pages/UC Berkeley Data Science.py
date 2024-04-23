import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time

st.title("UC Berkeley Master's in Data Science")

st.markdown("""
            The UC Berkeley Master's in Data Science (MIDS) program provided me with 
            a strong foundation in several facets of data science, such as basic Python and R coding,
            statistics, data engineering, data visualization, machine learning, ethics & privacy,
            and natural langauge processing.
            """)

st.markdown("""
            Feel free to use the following tabs to get a better understanding of the scope of each course along with corresponding projects and assignments I completed.
            """)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Intro to Python", "Research Design", 
                            "Statistics","Data Engineering",
                            "Machine Learning","Data Visualization",
                            "Behind the Data","Natural Language Processing",
                            "Capstone"])

# Function to center subheaders
def centered_subheader(subheader_text, font_size=18):
    st.markdown(f"<h3 style='text-align: center;'>{subheader_text}</h3>", unsafe_allow_html=True)

with tab1:
   centered_subheader("Introduction to Python Programmnig")
   st.markdown("**Class Description:** An introduction to computer programming, using Python, tailored to the needs of data scientists.")
with tab2:
   centered_subheader("Research Design and Applications for Data and Analysis")
with tab3:
   centered_subheader("Statistics for Data Science")
with tab4:
   centered_subheader("Data Engineering")
with tab5:
   centered_subheader("Machine Learning")
with tab6:
   centered_subheader("Data Visualization")
with tab7:
   centered_subheader("Behind the Data: Humans and Values")
with tab8:
   centered_subheader("Natural Language Processing")
with tab9:
   centered_subheader("Capstone")   

   