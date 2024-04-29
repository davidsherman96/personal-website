import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
import time
from W200_Calcs import main_heatmap, main_bar_chart

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
   centered_subheader("Introduction to Python Programming")
   st.markdown("**Class Description:** An introduction to computer programming, using Python, tailored to the needs of data scientists.")
   st.markdown("**Key Libraries:** Pandas, NumPy, Matplotlib, Seaborn")
   st.divider()
   st.subheader("**Final Project**")
   st.markdown("""**Goal:** Conduct an exploratory data 
               analysis of a dataset of our choosing to answer a research question. """)
   st.markdown("""**Our Scope:** Using a primary dataset provided by the 
               National UFO Reporting Center (NUFORC), we sought to address various questions, including:""")
   st.markdown("1. What is the incidence of unidentified aerial phenomena (UAP) over time, and how do they vary geographically?")
   st.markdown("2. What times are most UAPs reported?")


   heatmap_code = """ # Function to create the heatmap using Seaborn
def create_heatmap(data):
    plt.figure(figsize=(12, 10))
    sns.heatmap(data, annot=True, cmap='YlGnBu', fmt='d')
    plt.xlabel('Decade')
    st.pyplot()

# Display the heatmap for the top 10 cities by events
def main_heatmap():
    create_heatmap(final_heatmap_cities_decades_top_10)
    """
   
   barchart_code = """#Seaborn bar chart for top 10 reported NUFORC event times
def create_bar_chart(data):
    plt.figure(figsize=(12,8))
    custom_palette = sns.color_palette("flare", len(data)).as_hex()[::-1]
    ax = sns.barplot(x='Time', y='Count', data=data, palette=custom_palette)
    plt.xticks(rotation='horizontal')
    st.pyplot()

# Display the bar chart
def main_bar_chart():
    create_bar_chart(time_full)
    """
   
   st.warning("""See below for a sample of our work. To view the entire code notebook, 
              project write-up, and presentation, feel free to view our GitHub repository [here](https://github.com/davidsherman96/berkeley_data_science_w200_intro_python_programming/tree/main)
              """)

   centered_subheader("<u>NUFORC Events Heatmap by Decades (Top 10 Cities)</u>")
   main_heatmap()
   with st.expander("See Heatmap Code:"):
      st.code(heatmap_code, language="python")

   centered_subheader("<u>Top 10 Times By Total Reported Events</u>")
   main_bar_chart()   
   with st.expander("See Bar Chart Code:"):
      st.code(barchart_code, language="python")

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

   