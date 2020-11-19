# CMPT 353 Project

Investigating Airport Data in North American Airports in the year preceding (and during) the COVID-19 pandemic.

## IMMEDIATE TO DO:
1. Get that github data and comb through daily reports to get ONLY Canada and US from csse_covid_19_data folder → csv files, plus one column = worldwide total **(Done)**
    - Cutoff dates: '2020-03-16' to '2020-10-16' ← to match w/ kaggle airport data
    - Turn into one (or 2?) dataframe/file for case_counts
2. Somehow download kaggle data and turn it into something
    - A file that can be accessed by the next Python Program
3. Create Python program that looks at those two files and do analysis
    - Idk we figure later whoever gets this part will figure it out :)
    - First we visualize the data 
    - Then we do some ML 

## Timeline
- When are we going to do this? → very suggestive
- Get some dataframes by November 23rd.
- Get some ML by Nov 30th
- Get some words by December 7th 
- Project due December 11th

## COVID Data
- Discard Diamond Princess Cruise cases (This was in Japan, but there were infected Americans and Canadians)
- What about Grand Princess? (Happened in USA)
- Leave out US Virgin Islands? (i.e. Puerto Rico)
- Figure out how to interpret data and make it workable
- Needs further cleaning; check for possibility of imbalanced data

## Machine Learning
- Figure out approach/question
- Regression to find airport pecentage baseline values
    - Add extra features to covid data set 
- Supervised Learning
    - Treat as Classification -> Increase in traffic, decrease in traffic etc.
    - Regression -> Produce PercentofBaseline values
- Unsupervised Learning
    - Clustering