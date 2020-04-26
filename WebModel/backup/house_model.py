# -*- coding: utf-8 -*-
"""House_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TvBcmgjQwUZnjNJRi1whrTKaLlA7HEJd
"""

# Machine Learning Framework: KDD / SEMMA (1996)
# SEMMA: Sample, Explore, Modify, Model, Assess
# Objective: Acquire knowledge out of house dataset provided
# Purpose: House price prediction
# Datapoint: http://hackveda.in/sistec/Housing_Modified.csv
# Source: Boston City

# 1. Sample 
import pandas as pd
data = pd.read_csv("http://hackveda.in/sistec/Housing_Modified.csv")
data.head(5)

# 2. Explore
# Plot the variables / attributes in data
#print(data.columns)
#data.plot()

# Explore
# Check the correlation of all attributes / variables in sample
data.corr()

# Check the shape of dataset
data.shape

# 3. Modify 
# Convert string to numeric 
# 3a. Convert binary category to numeric using Label Binarizer
import sklearn.preprocessing as pp
lb = pp.LabelBinarizer()
data.driveway = lb.fit_transform(data.driveway)
data.recroom = lb.fit_transform(data.recroom)
data.fullbase = lb.fit_transform(data.fullbase)
data.gashw = lb.fit_transform(data.gashw)
data.airco = lb.fit_transform(data.airco)
data.prefarea = lb.fit_transform(data.prefarea)
data.head(2)

# Modify
# 3b. Convert n-categorical string attributes / variables into numeric
# Technique: One-Hot Encoding using Dummy Indicator Variables
data_stories = pd.get_dummies(data.stories, prefix="stories")

# Shape of data before concatenation
data.shape

# Concatenate data with data_stories and remoove stories string category column
data = pd.concat([data, data_stories], axis=1)

# Remove the string category stories
del data["stories"]

# Check the shape of data after modification
data.shape

# Show the columns
#print(data.columns)

# Show the top 3 observations from data
data.head(3)

# 4. Model - Data Mining 
# Check the Key Performing Indicators 

# 4a. Show the correlation matrix to check all key performing indicators
data.corr()

# 4. Modify 
# Create a correlation matrix or a heatmap visual correlation computation
import seaborn as sns
#sns.heatmap(data.corr(), annot=True, square=True, fmt='.1f')

# 4. Model
import statsmodels.api as sm

response = data["price"] # dependent variable ( Y )
independent = data.columns
independent = independent.delete(0) # Delete price column from independent

#print("Response variable", response)
#print("Independent variable", independent)

Y = data["price"]
X = data[independent]
ols_model = sm.OLS(Y, X).fit() # calculate m and c using actual values of Y & X

predicted_price = ols_model.predict(X)

# equation: Y = m1X1 + m2X2 + .... mnXn + c

# fit stage:
# calculation of m1, m2, m3 .... mn and c is done in this stage using actual Y(price), X(independent)

# predict stage
# Y1 = mX1 + c [ Y1 = predicted_price ]


# 5. Assess
# Compared actual price vs predicted price to check accuracy using R-squared
#ols_model.summary()

# Implementation of variance inflation factor for multicollinearity removal
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
type(X)

# Convert dataframe to ndarray
x_array = X.values
type(x_array)

# Implementation of multi-collinearity removal
for i in range(len(independent)):
    mvif = [vif(X[independent].values, index) 
            for index in range(len(independent))]
    max_vif = max(mvif)
    dindex = mvif.index(max_vif)
    #print("Index", dindex, "MaxVIF", max_vif, "Column", independent[dindex])
    if max_vif > 10:
        independent = independent.delete(dindex)
#print(independent)

Y = data["price"]
X_new = data[independent]
ols_model_1 = sm.OLS(Y, X_new).fit()
ols_model_1.summary()

predict_price_1 = ols_model_1.predict(X_new)

# Make a dataframe with three columns
# actual price, predicted_price(65) and predict_price_1(95)
sample_df = pd.DataFrame()
sample_df["Actual"] = data["price"]
sample_df["Predict_65"] = ols_model.predict(X)
sample_df["Predict_95"] = ols_model_1.predict(X_new)
sample_df

# Plot the graph with Actual, Predicted_65 and Predicted_95
'''import matplotlib.pyplot as plt
plt.scatter(X.lotsize, sample_df["Actual"], color="blue")
plt.scatter(X.lotsize, sample_df["Predict_65"], color="red")
plt.scatter(X.lotsize, sample_df["Predict_95"], color="green")

plt.xlabel("Lotsize")
plt.ylabel("Price")
plt.title("House price model comparison")
'''


# 29 January 2019 Session Live
# Objectives:
# 1. Create a simple cli app to ask info from users
# and predict the house price

# How to take user input 
# lotsize = input("Enter lotsize: ")
#print("The lotsize of house is", lotsize)

# bathrms = int(input("Enter bathrooms:"))
#print("Number of bathrooms in house", bathrms)

# Check the type of input
#print("The type of lotsize is", type(lotsize))
#print("The type of bathrms is", type(bathrms))

# Convert input string into numbers using int()

# Ask users about the information for independent variables
#ols_model_1.summary()



# Create a dataframe using dictionary and add values to index zero



# Ask for independent variables from user
import sys
# create an empty dictionary

independent = ['lotsize', 'bathrms', 'driveway','recroom', 
                         'fullbase', 'gashw', 'airco', 'garagepl', 
                         'prefarea', 'stories_four', 
                         'stories_one','stories_three']


lotsize = int(sys.argv[1])
bathrms = int(sys.argv[2])
driveway = int(sys.argv[3])
recroom =int(sys.argv[4])
fullbase =int(sys.argv[5])
gashw = int(sys.argv[6])
airco = int(sys.argv[7])
garagepl = int(sys.argv[8])
prefarea = int(sys.argv[9])
stories_four = int(sys.argv[10])
stories_one = int(sys.argv[11])
stories_three= int(sys.argv[12])

dict1 = {'lotsize':lotsize , 'bathrms':bathrms , 'driveway':driveway, 'recroom':recroom,'fullbase':fullbase,
       'gashw':gashw , 'airco':airco , 'garagepl':garagepl , 'prefarea':prefarea,
       'stories_four':stories_four , 'stories_one':stories_one,'stories_three':stories_three}

user_data = pd.DataFrame(data=dict1, index=[0], columns=independent)
# Predict price of house for current user_data
price = ols_model_1.predict(user_data)
#print("Predicted house price is: USD", round(price[0]))
#print("Predicted house price is: USD", int(price[0]))
print("USD", int(price[0]))
