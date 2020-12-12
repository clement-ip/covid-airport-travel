# CMPT 353 Final Project

Topic: Investigating Airport Data in North American Airports in the year preceding (and during) the COVID-19 pandemic.

Contributors: Anna Tang, Clement Ip, Erica Ho

## Instructions:

Required Libraries:
```
pip install scipy pandas numpy matplotlib seaborn sklearn scipy geopandas contextily contextily
```

Work for each airport can be viewed by running its respective .ipynb notebook file.

## Output

In this project we develop machine learning models that extrapolate and predict how airport traffic will fare in YVR, YEG, YYZ, and YUL during the pandemic. We also analyze the correlation between airport traffic and the number new cases per day, as well as the cumulative number of confirmed cases. 

Results of our analyze can be viewed by running each of the available .ipynb notebook files.

## File Directory 

```
353project
├── Airport-Data -> Contains the airport traffic data for each airport.
├── Archived-Data -> Contains the scripts used to filter and produce dataframes for analysis.
├── Covid-Data -> Contains the COVID-19 numbers for each province.
├── analyze_covid_hubs.ipynb -> An intial examination of the province's Covid situation.
├── analyze_airport_hubs.ipynb -> An intial examination of the airport's traffic trend.
├── analyzeYEG.ipynb
├── analyzeYUL.ipynb
├── analyzeYVR.ipynb
├── analyzeYYZ.ipynb
```
