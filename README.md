# CMPT 353 Project

Investigating Airport Data in North American Airports in the year preceding (and during) the COVID-19 pandemic.

## Navigating the Repository
-  Do work on `analyze_airport_hubs.ipynb`, `analyze_covid_hubs.ipynb` and `analyze_both.ipynb`
- `scrap_*.ipynb` files can be ignored (not deleted yet because it might be useful idk)
- `analyze_airport_hubs.ipynb` contains the code to generate `*4analyze_both.csv` 
- `analyze_covid_hubs.ipynb` contains the code to generate `*-modified.csv`
    - use `index = False` in `.to_csv()` to resolve the random `unamed` columns being generated
- If any of the source data is messed up, go into the scrap notebooks to regenerate a new instance and fix accordingly
    - covid cases -> ` scrap_analyze_covid.ipynb` and `make_params_for_covid.ipynb`


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
- Analyze Statistical significance of relation between case counts and airport data

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


