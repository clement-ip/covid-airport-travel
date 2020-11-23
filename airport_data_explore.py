#!/usr/bin/env python
# coding: utf-8

# # Data Exploration

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import shapely


# In[4]:


# Proportion of trips on this date as compared to Avg number of trips on the same day of week in baseline period i.e 1st


# In[5]:


df = pd.read_csv("covid_impact_on_airport_traffic.csv")


# In[6]:


df


# In[7]:


countries = df.groupby(["Country"])["Country"].count().reset_index(name = "Count Country")


# # Retrieve Long and Lat Coordiantes
# 

# In[6]:


def getLat(point):
    _, lat = point[6:-1].split(" ")
    return float(lat)


# In[7]:


def getLong(point):
    long, _ = point[6:-1].split(" ")
    return float(long)


# In[8]:


df["lat"] = df["Centroid"].map(getLat)
df["long"] = df["Centroid"].map(getLong)


# In[9]:


df


# In[8]:


# split dataframe into USA and CA
canada = df.loc[df["Country"] == "Canada"]
usa = df.loc[df["Country"] == "United States of America (the)"]
temp = [usa, canada]
na = pd.concat(temp)


# In[9]:


# cities in CA and USA
canadaCities = canada.groupby(["City"])["City"].count().reset_index(name = "Count City")
usaCities = usa.groupby(["City"])["City"].count().reset_index(name = "Count City")
naCities = na.groupby(["City"])["City"].count().reset_index(name = "Count City")


# In[10]:


rankNA = na.groupby("AirportName").mean().sort_values(by = "PercentOfBaseline")
rankCA = canada.groupby("AirportName").mean().sort_values(by = "PercentOfBaseline")
rankUSA = usa.groupby("AirportName").mean().sort_values(by = "PercentOfBaseline")

# # Plot Coordinates of Airports in North America

# In[15]:

'''
# Refer to geopandas documentation: https://geopandas.org/gallery/create_geopandas_from_pandas.html
world = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres')
)


# In[16]:


# Make 'Geometry' in NA dataframe; will have to refactor this later on (code is messy, have three cols of the same thing)
gdfna = gpd.GeoDataFrame(na, geometry = gpd.points_from_xy(na.long, na.lat))


# In[17]:


# Plot coordinates onto map of NA
ax = world[world.continent == 'North America'].plot(color='white', edgecolor='black')
gdfna.plot(ax = ax, color = 'blue', markersize = 10)
plt.savefig('na.svg')
#plt.show()


# # Find Outliers 

# In[18]:


canada.boxplot(column = ['PercentOfBaseline'], by = 'AirportName', rot = 90, fontsize = 10, figsize = (18,10))


# In[19]:


usa.boxplot(column = ['PercentOfBaseline'], by = 'AirportName', rot = 90, fontsize = 10, figsize = (25,15))
'''

# In[20]:


# Find monthly outliers of YVR 
canada['Date'] = pd.to_datetime(canada['Date'])
yvr = canada.loc[canada['AirportName'] == 'Vancouver International']


# In[21]:


# https://stackoverflow.com/questions/44908383/how-can-i-group-by-month-from-a-date-field-using-python-pandas/44908576
yvr.groupby(yvr['Date'].dt.strftime('%b'))['PercentOfBaseline'].mean().sort_values


# In[22]:

'''
yvr.boxplot(column = ['PercentOfBaseline'], by = yvr['Date'].dt.strftime('%b'), rot = 90, fontsize = 10, figsize = (25,15))
plt.suptitle("")
plt.xlabel("")
# Repeat this for all NA airports?
'''

# #Exporting Daily numbers to CSV file

# In[23]:


na.reset_index(inplace=True)
naDailyData = na[['Date', 'AirportName', 'PercentOfBaseline', 'City','State','Country', 'lat','long']]
naDailyData.to_csv('airport_traffic_NA.csv')

