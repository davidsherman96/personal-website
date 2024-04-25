import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# nuforc_events_clean = pd.read_csv('nuforc_events_clean.csv', index_col=0)
# airports_clean = pd.read_csv('airports_clean.csv')
# military_bases_clean = pd.read_csv('MilitaryBases_clean.csv')
# space_launch_data_clean = pd.read_csv('space_launch_data_clean.csv')

# nuforc_events_clean['Date_Clean'] = pd.to_datetime(nuforc_events_clean['Date'])
# nuforc_events_clean['Year'] = nuforc_events_clean['Date_Clean'].dt.year

# #Creating concatenated field for city & state to account for certain city names that may be used more than once across the U.S.
# nuforc_events_clean['City_State'] = nuforc_events_clean['City'] + ', ' + nuforc_events_clean['State']

# #Creating new dataframe to look at counts by city
# nuforc_events_city_state_counts = nuforc_events_clean['City_State'].value_counts().reset_index().head(10)
# nuforc_events_city_state_counts.columns = ['City_State','Event_Counts']

# #Seaborn bar chart for top 10 cities
# plt.figure(figsize=(12,8))
# ax = sns.barplot(x='City_State', y='Event_Counts', data=nuforc_events_city_state_counts)
# plt.xticks(rotation='45')
# plt.title('Top 10 Cities By Events')
# plt.show()