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

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Intro to Coding", "Research Design", 
                            "Statistics","Data Engineering",
                            "Machine Learning","Data Visualization",
                            "Behind the Data","Natural Language Processing",
                            "Capstone"])

with tab1:
   st.header("Introduction to Python Programmnig")
with tab2:
   st.header("Research Design and Applications for Data and Analysis")
with tab3:
   st.header("Statistics for Data Science")
with tab4:
   st.header("Data Engineering")
with tab5:
   st.header("Machine Learning")
with tab6:
   st.header("Data Visualization")
with tab7:
   st.header("Behind the Data: Humans and Values")
with tab8:
   st.header("Natural Language Processing")
with tab8:
   st.header("Capstone")   

   