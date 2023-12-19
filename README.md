# Amazon Project

Link to Dataset --> https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset

Data Visualization, Data Analysis

# Liberaries
pandas
seaborn
matplotlib

# About
This is a dataset about Amazon products price 

# Objective
1. Find which category and sub category attract more buyers
2. Find which top 10 manufacturers sell the most
3. Find any relationship between manufacturers/ ratings/ actual price/ discount price
 
# Method
Apply data cleaning steps
Analyze data and create data vizualization using matlabplot and searborn

# Conclusion
After this EDA (Exploratory Data Analysis):

* Most popular manufacturers on Amazon are :Pc, Puma, Shopnet, Amazon, U.S, The, Nike, Avsar, Van, Neutron
* Ratings of those 10 manufacturers is mosltly between 0 and few between 3 - 5  which means something is wrong ,usually big brands have between 4 and 5 ratings ,this can be explained by : 
    . Dirty Data ( inaccurate data)
    . While cleaning data i filled all null values from ratings and no_of_ratings with 0

* Men's clothing and accessories are the most popular categories / sub categories 
* No correlation between ratings/no_of_ratings discount_price/actual_price ( This probably is because of what was said above) normally we tend to see strong correlation between no_of_ratings and discount_price for example or even  actual_price/ ratings for top 10 manufacturers 

