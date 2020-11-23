#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import shapely
import seaborn as sns


# In[2]:


# 


# In[3]:


dfNA = pd.read_csv('casesNA.csv',compression = 'gzip')
dfCA = pd.read_csv('casesCanada.csv',compression = 'gzip')
dfUS = pd.read_csv('casesUS.csv',compression = 'gzip')


# In[4]:


# Generate list of provinces, states, states + counties looked at
provs = dfCA.groupby(["Province/State"])["Province/State"].count().reset_index(name = "Count")
states = dfUS.groupby(["Province/State"])["Province/State"].count().reset_index(name = "Count")
counties = dfUS.groupby(["County", "Province/State"])["County"].count().reset_index(name = "Count")


# In[5]:


# counties.sort_values(by = "Province/State")


# In[6]:


# states


# In[7]:


# provs


# In[8]:

'''
world = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres')
)
gdfus = gpd.GeoDataFrame(dfUS, geometry = gpd.points_from_xy(dfUS.Longitude, dfUS.Latitude))
gdfca = gpd.GeoDataFrame(dfCA, geometry = gpd.points_from_xy(dfCA.Longitude, dfCA.Latitude))


# In[9]:


# Interesting.... find a way to make them less ugly 
ax = world[world.name == 'United States of America'].plot(color='white', edgecolor='black')
gdfus.plot(ax = ax, color = 'blue', markersize = 1)
plt.show()


# In[10]:


ax = world[world.name == 'Canada'].plot(color='white', edgecolor='black')
gdfca.plot(ax = ax, color = 'blue', markersize = 1)
plt.show()


# In[11]:

'''
# Refer to features here: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data
totalCan = dfCA.groupby(["Province/State", "Date"])["Confirmed"].sum().reset_index(name = "Count")


# In[12]:


temp = totalCan.shift(1)
totalCan['Difference'] = totalCan['Count'] - temp['Count']


# In[13]:


# Group by provinces; find difference in cases between the next day and day before
# Neg diff: did someone die or recover? Correction in case count?
# 0 diff: no increase or decrease
# totalCan


# In[14]:


totalUS = dfUS.groupby(["Province/State", "Date"])["Confirmed"].sum().reset_index(name = "Count")


# In[15]:


temp = totalUS.shift(1)
totalUS['Difference'] = totalUS['Count'] - temp['Count']


# In[16]:


nyCount = totalUS.loc[(totalUS["Province/State"] == "New York")].reset_index(drop = True)
bcCount = totalCan.loc[(totalCan["Province/State"] == "British Columbia")].reset_index(drop = True)


# In[17]:


# TODO: Set each march 22 2020 to NaN
# Hardcoded for now
nyCount.loc[0, "Difference"] = np.NaN
bcCount.loc[0, "Difference"] = np.NaN


# In[18]:

'''
# TODO: Fix graph
plt.figure(figsize = (20,5))
plt.ylim(0,550)
plt.xlabel("Mid-March to Mid October")
plt.ylabel("# of New Cases")
plt.plot(bcCount["Date"], bcCount["Difference"])


# In[20]:


plt.figure(figsize = (20,5))
plt.xlabel("Mid-March to Mid October")
plt.ylabel("# of New Cases")
plt.plot(nyCount["Date"], nyCount["Difference"])


# In[27]:


# A shitshow 
plt.figure(figsize=(40, 5))
records = sns.countplot(data = dfNA, x="Combined_Key",
              order = dfNA['Combined_Key'].value_counts().index)
records.set_xticklabels(records.get_xticklabels(), rotation=90)

'''
# In[34]:


# BC usually does not report case count on weekends. This may result in a spike on Mondays.
# Verify integrity of data.

# Check for # of weekends reported for BC
bcCount['Date'] = pd.to_datetime(bcCount['Date'])
bcCount['Weekday'] = bcCount['Date'].dt.day_name()

bcDayCount = pd.DataFrame(bcCount['Weekday'].value_counts())
dayRecords = bcDayCount.plot.pie(y = 'Weekday', figsize = (7,7))
# Result: It seems like there are published results on weekends.


# In[39]:


bcCount.drop(columns = ['Weekday'])
bcCount['Month'] = bcCount['Date'].dt.month_name()
# Produce averages 
bcCount.groupby(['Month']).mean()




