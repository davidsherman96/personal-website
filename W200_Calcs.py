import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Creating the dataframes for EDA
nuforc_events_clean = pd.read_csv('nuforc_events_clean.csv', index_col=0)
airports_clean = pd.read_csv('airports_clean.csv')
military_bases_clean = pd.read_csv('MilitaryBases_clean.csv')
space_launch_data_clean = pd.read_csv('space_launch_data_clean.csv')

#Section 1 - Creating heatmap for NUFORC events by city over time

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
    sns.heatmap(data, annot=True, cmap='flare', fmt='d')
    plt.xlabel('Decade')
    st.pyplot()

# Display the heatmap
def main_heatmap():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    create_heatmap(final_heatmap_cities_decades_top_10)

#############################################
#Section 2 - Creating bar chart of counts of NUFORC events by hour

#Creating new dataframe, filtering out rows that have NaNs for hour and minute fields
time_fix = nuforc_events_clean.dropna(subset=['Hour','Minute'])

#Converting hours and minutes to ints
time_fix['Hour'] = time_fix['Hour'].astype(int)
time_fix['Minute'] = time_fix['Minute'].astype(int)

#Creating function that will allocate an A.M. or P.M. value based on the army time ('Hour' field) given in the NUFORC data 
def am_pm(value):
    if value >= 0 and value <= 12:
        return 'A.M.'   
    else:
        return 'P.M.'


#Apply AM_PM function to create a new column    
time_fix['AM_PM'] = time_fix['Hour'].map(am_pm)


#Create hour dictionary to convert army time to standard time equivalent, then apply dictionary replacement function
hour_dict = {0:12, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11,
            12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11}

time_fix['Hour'] = time_fix['Hour'].replace(hour_dict)

#Create minute dictionary to account for single digit minutes, then apply dictionary replacement function
minute_dict = {0:'00', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}

time_fix['Minute'] = time_fix['Minute'].replace(minute_dict)

#New column with the cleaned up time field
time_fix['Full_Time'] = time_fix['Hour'].astype(str) + ':' + time_fix['Minute'].astype(str) + ' ' + time_fix['AM_PM']

#New dataframe for 10 most popular times of day by event count
time_full = time_fix['Full_Time'].value_counts().reset_index().head(10)
time_full.columns = ['Time','Count']

#Seaborn bar chart for top 10 reported NUFORC event times
def create_bar_chart(data):
    plt.figure(figsize=(12,8))
    custom_palette = sns.color_palette("flare", len(data)).as_hex()[::-1]
    ax = sns.barplot(x='Time', y='Count', data=data, palette=custom_palette)
    plt.xticks(rotation='horizontal')
    # plt.title('Top 10 Times By Total Reported Events')
    st.pyplot()

# Display the bar chart
def main_bar_chart():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    create_bar_chart(time_full)
