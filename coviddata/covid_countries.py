#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys, os
import glob


# In[2]:


# Take all 217 csv files and merge it into one big dataframe
# Eventually we would want to split the dataframe into three csvs - 
# canada, usa, and north america


# In[3]:


# Retrieved from: https://stackoverflow.com/questions/58274401/importing-multiple-csv-files-into-pandas-and-merge-them-into-one-dataframe
path = os.getcwd() # Find path of current working directory
all_files = glob.glob(path + "/*.csv")
dfs = list()

# Add all data files into one list and merge into one big df
for file in all_files:
    df = pd.read_csv(file)
    
    # Fix columns with different names but same content
    # i.e. Country_Region -> Country/Region
    if set(['FIPS','Admin2']).issubset(df.columns):
        df = df.drop(['FIPS', 'Admin2'], axis = 1)
    if 'Province_State' in df:
        df = df.rename(columns = {'Province_State': 'Province/State'})
    if 'Country_Region' in df:
        df = df.rename(columns = {'Country_Region': 'Country/Region'})
    if 'Last_Update' in df:
        df = df.rename(columns = {'Last_Update': 'Last Update'})
    if 'Lat' in df:
        df = df.rename(columns = {'Lat': 'Latitude'})
    if 'Long_' in df:
        df = df.rename(columns = {'Long_': 'Longitude'})
    dfs.append(df)

frame = pd.concat(dfs, ignore_index = True, axis = 0)


# In[4]:

# North America Cases - US/NA, not counting the Diamond Princess Cruise cases
# Omit Grand Princess cruise cases?
frame_filtered = frame.loc[(frame["Country/Region"] == "US") | (frame["Country/Region"] == "Canada")]
frame_filtered = frame_filtered.loc[(frame_filtered["Province/State"] != "Diamond Princess")].reset_index(drop = True)

# In[ ]:


# Canada Cases
casesCanada = frame_filtered.loc[(frame_filtered["Country/Region"] == "Canada")].reset_index(drop = True)

# USA Cases 
casesUS = frame_filtered.loc[(frame_filtered["Country/Region"] == "US")].reset_index(drop = True)

casesNA = frame_filtered

# Convert dataframes into CSVs
casesNA.to_csv('casesNA.csv', index = False, compression ='gzip')
casesUS.to_csv('casesUS.csv', index = False, compression ='gzip')
casesCanada.to_csv('casesCanada.csv', index = False, compression ='gzip')