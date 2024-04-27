import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nuforc_events_clean = pd.read_csv('nuforc_events_clean.csv', index_col=0)
airports_clean = pd.read_csv('airports_clean.csv')
military_bases_clean = pd.read_csv('MilitaryBases_clean.csv')
space_launch_data_clean = pd.read_csv('space_launch_data_clean.csv')


nuforc_events_clean['Date_Clean'] = pd.to_datetime(nuforc_events_clean['Date'])
nuforc_events_clean['Year'] = nuforc_events_clean['Date_Clean'].dt.year

#Creating concatenated field for city & state to account for certain city names that may be used more than once across the U.S.
nuforc_events_clean['City_State'] = nuforc_events_clean['City'] + ', ' + nuforc_events_clean['State']

#Creating new dataframe to look at counts by city
nuforc_heatmap = nuforc_events_clean[['City_State', 'State','Year']].value_counts().reset_index()
nuforc_heatmap.columns = ['City_State','State','Year','Events']

heatmap_1970s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 1970) & (nuforc_heatmap['Year'] <= 1979)].reset_index(drop=True)
heatmap_1970s = heatmap_1970s.rename({'Events': '1970s'}, axis=1)

heatmap_1980s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 1980) & (nuforc_heatmap['Year'] <= 1989)].reset_index(drop=True)
heatmap_1980s = heatmap_1980s.rename({'Events': '1980s'}, axis=1)

heatmap_1990s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 1990) & (nuforc_heatmap['Year'] <= 1999)].reset_index(drop=True)
heatmap_1990s = heatmap_1990s.rename({'Events': '1990s'}, axis=1)

heatmap_2000s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 2000) & (nuforc_heatmap['Year'] <= 2009)].reset_index(drop=True)
heatmap_2000s = heatmap_2000s.rename({'Events': '2000s'}, axis=1)

heatmap_2010s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 2010) & (nuforc_heatmap['Year'] <= 2019)].reset_index(drop=True)
heatmap_2010s = heatmap_2010s.rename({'Events': '2010s'}, axis=1)

heatmap_2020s = nuforc_heatmap[(nuforc_heatmap['Year'] >= 2020) & (nuforc_heatmap['Year'] <= 2022)].reset_index(drop=True)
heatmap_2020s = heatmap_2020s.rename({'Events': '2020s'}, axis=1)

heatmap_1970s_groupby = heatmap_1970s[['1970s','City_State']].groupby('City_State').agg(sum)
heatmap_1980s_groupby = heatmap_1980s[['1980s','City_State']].groupby('City_State').agg(sum)
heatmap_1990s_groupby = heatmap_1990s[['1990s','City_State']].groupby('City_State').agg(sum)
heatmap_2000s_groupby = heatmap_2000s[['2000s','City_State']].groupby('City_State').agg(sum)
heatmap_2010s_groupby = heatmap_2010s[['2010s','City_State']].groupby('City_State').agg(sum)
heatmap_2020s_groupby = heatmap_2020s[['2020s','City_State']].groupby('City_State').agg(sum)

merge_70s_80s = pd.merge(heatmap_1970s_groupby, heatmap_1980s_groupby, on ='City_State', how ='left')
merge_80s_90s = pd.merge(merge_70s_80s, heatmap_1990s_groupby, on = 'City_State', how = 'left')
merge_90s_00s = pd.merge(merge_80s_90s, heatmap_2000s_groupby, on = 'City_State', how = 'left')
merge_00s_10s = pd.merge(merge_90s_00s, heatmap_2010s_groupby, on = 'City_State', how = 'left')
merge_10s_20s = pd.merge(merge_00s_10s, heatmap_2020s_groupby, on = 'City_State', how = 'left')


merge_10s_20s['Sum_Events'] = merge_10s_20s.sum(axis=1)
final_heatmap_cities_decades = merge_10s_20s.replace(np.nan,0)

final_heatmap_cities_decades = final_heatmap_cities_decades.astype({'1980s': 'int','1990s': 'int',
                                                                '2000s': 'int','2010s': 'int',
                                                                '2020s': 'int','Sum_Events': 'int'})

final_heatmap_cities_decades.sort_values(by='Sum_Events',ascending=False)
final_heatmap_cities_decades_top_10 = final_heatmap_cities_decades.sort_values(by='Sum_Events',ascending=False).head(10)
final_heatmap_cities_decades_top_10.drop(['Sum_Events'], axis=1, inplace=True)

 # Function to create the heatmap using Seaborn
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

# if __name__ == "__main__":
#     main()