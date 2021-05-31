from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import time
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv('vinData.csv')
yearMask = df['Year'] < 2022
dfClean = df[yearMask]

def get_distribution_of_ratings():
    dfratings = dfClean.Rating.unique()
    ratings = dfratings.sort()

    plotdata = pd.DataFrame(0, index=dfratings, columns=['Count'])

    loop = 0
    for r in dfratings: 
        for row in dfClean['Rating']:
            if(row == r):
                plotdata['Count'].iloc[loop] = plotdata['Count'].iloc[loop] + 1
        loop += 1

    plt.style.use('ggplot')
    plt.figure(figsize=(10, 10))
    x = plotdata.index
    y = plotdata['Count']
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, y, color='green')
    plt.xlabel("Ratings")
    plt.ylabel("Number of ratings")
    plt.title("Overview of number of ratings per rating")

    plt.xticks(x_pos, x)
    plt.show()
    

def get_seaborn_chart():
    return sb.pairplot(dfClean)

def get_correlation():
    return dfClean.corr()

def plot_price_and_rating_correlation():
    x = dfClean['Price']
    y = dfClean['Rating']

    plt.scatter(x, y, color='g')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red')
    correlation = x.corr(y)
    plt.xlabel('Price')
    plt.ylabel('Rating')
    print(correlation)
    
def plot_year_and_rating_correlation():
    x = dfClean['Year']
    y = dfClean['Rating']
    plt.scatter(x, y, color='g')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red')
    correlation = x.corr(y)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    print(correlation)
    
def improvement_in_correlation_over_time():
    print(len(dfClean))
    for size in range(300, 3200, 200):
        print("Correlation ved størrelse " + str(size) + ": " + str(dfClean['Year'][0:size].corr(dfClean['Rating'][0:size])))
    
def price_linear_correlation():
    x = (dfClean['Price'].values).reshape(-1,1)
    y = (dfClean['Rating'].values)
    reg = LinearRegression().fit(x, y)

    print("Sklearn LinearRegression score på korrelationen: " + str(reg.score(x, y))) 
    print("Koefficienten: + " + str(reg.coef_))
    print("Konstanten: " + str(reg.intercept_))

    print(reg.predict([[450]]))
    print("Vi kan forvente at en vin til prisen 450. har en rating på:"); print(0.00056345 * 450 + 3.81)
    

def predict_prices():
    x = (dfClean['Price'].values).reshape(-1,1)
    y = (dfClean['Rating'].values)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    reg = LinearRegression()
    reg.fit(X_train, y_train)

    y_pred = reg.predict(X_test)

    dfTrain = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    dfTrain

    print(dfTrain[60:75])
    r2_score(dfTrain['Actual'], dfTrain['Predicted'])
