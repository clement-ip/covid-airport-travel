# CMPT 353 Project

Investigating Airport Data in North American Airports in the year preceding (and during) the COVID-19 pandemic.

## IMMEDIATE TO DO (pls update):
1. Get that github data and comb through daily reports to get ONLY Canada and US from csse_covid_19_data folder → csv files, plus one column = worldwide total **(Done)**
    - Cutoff dates: '2020-03-16' to '2020-10-16' ← to match w/ kaggle airport data
    - Turn into one (or 2?) dataframe/file for case_counts
2. Somehow download kaggle data and turn it into something **(Done??)**
    - A file that can be accessed by the next Python Program
3. Create Python program that looks at those two files and do analysis
    - Idk we figure later whoever gets this part will figure it out :)
    - First we visualize the data 
    - Then we do some ML 
4. is there a relation between case count and baseline? Is it statistically significant?

## Timeline
- When are we going to do this? → very suggestive
- Get some dataframes by November 23rd.
- Get some ML by Nov 30th
- Get some words by December 7th 
- Project due December 11th

## COVID Data
- Outliers **Done**
    - Discard Diamond Princess Cruise cases (This was in Japan, but there were infected Americans and Canadians)
    - What about Grand Princess? (Happened in USA)
    - Leave out US Virgin Islands? (i.e. Puerto Rico)
- Figure out how to interpret data and make it workable
- **Check for possibility of imbalanced data**

## Airports Data
- USA/Canada airport groupings done
- **TODO: Need to seperate into their own/each respective group or dataframe. Export as .csv? Figure out what works best with ML**
- **TODO: Canada - Figure out what to do for missing provinces/territories**

## Machine Learning
- Figure out approach/question
- Regression to find airport pecentage baseline values
    - Add extra features to covid data set 
- Supervised Learning
    - Treat as Classification -> Increase in traffic, decrease in traffic etc.
    - Regression -> Produce PercentofBaseline values
- Unsupervised Learning
    - Clustering    
- Possible Ideas/Approachs
    - Pretend we are Air Canada or some American airline. Determine how many planes to send out to certain destination within US and Canada, or we should increase/decrease/preserve the number of flights to the destination.
    - ^ or if it is a good idea to plan flights at all to that destination
    - ~~Predictions for when covid vaccines come out~~

## Other notes:
### Assumptions
- Travellers went to the nearest airport to their county (USA)
- All of ontario went to Toronto... etc
- make it domestic travel only? given travel ban


## Problem Statement (put this onto the report later)

Problem Statement:

Team ACE is commissioned by Air Canada and Delta Airlines to determine how they should circulate flights during the trying times of the pandemic. They would like us to produce a machine learning model that predicts how air traffic would fare in their main airport hubs*. In the event of a wave of infections, would people prefer to stay where they are or would they want to take the first flight home? What would people do if the curve of infections flatten?

It is difficult to guarantee a prediction of exact percentages of airport traffic (compared pre-pandemic rates from 1st February to 15th March 2020) or give an estimate of how many flights they should send out. We compromised with these airlines, and promised that we could give them general guidance on whether they should decrease, increase or maintain the number of flights based on the extrapolated traffic percentage of pre-pandemic numbers. 

Airline Hubs - 
Air Canada:
Calgary
Montreal Trudeau
Toronto Pearson
Vancouver

Delta Airlines:
Atlanta
Los Angeles
New York (JFK)
Seattle
