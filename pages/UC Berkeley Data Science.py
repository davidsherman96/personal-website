import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time
from W200_Calcs import main_heatmap

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
   st.markdown("**Key Libraries:** Pandas, NumPy, Matplotlib")
   st.divider()
   st.subheader("**Final Project**")
   st.markdown("""**Goal:** Conduct an exploratory data 
               analysis of a dataset of our choosing to answer a research question. """)
   st.markdown("""**Our Scope:** Using a primary dataset provided by the 
               National UFO Reporting Center (NUFORC), we sought to address the following questions:""")
   st.markdown("1. What is the incidence of unidentified aerial phenomena (UAP) over time, and how do they vary geographically?")
   st.markdown("2. Does the geographical distribution of UAPs correlate with commercial space launch sites, with military base locations, and/or with commercial airport locations?")
   st.markdown("3. What are the reported shapes of UAPs, and does this vary by year or states?")
   st.markdown("4. What is the duration of reported UAP events, and has this changed over the years?")
   code = """ # Function to create the heatmap using Seaborn
def create_heatmap(data):
    plt.figure(figsize=(12, 10))
    sns.heatmap(data, annot=True, cmap='YlGnBu', fmt='d')
    plt.xlabel('Decade')
    st.pyplot()

# Streamlit app
def main_heatmap():
    st.title('NUFORC Events Heatmap by Decades (Top 10 Cities)')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Display the heatmap for the top 10 cities by events
    create_heatmap(final_heatmap_cities_decades_top_10)
    """
   st.code(code, language="python")
   main_heatmap()
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

   