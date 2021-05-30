import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import time

df = pd.read_csv('vinData.csv')
year_review_mask = (df['Year'] < 2022) & (df['Reviews'] > 0)
dfClean = df[year_review_mask]

#dfClean.head()

data_chart = dfClean.drop(columns=('Price'))
#data_chart.head()


#Test index på vin
data_chart.loc[116]


def max_rating_df(df):
    m = data_chart.groupby('Year')['Rating'].transform('max') == data_chart['Rating']
    dfmax = data_chart.loc[m]
    max_rating = dfmax.sort_values('Year')
    maxdf = max_rating.drop_duplicates()
    return maxdf

    
max_df = data_chart.copy()
maxdfdf = max_rating_df(max_df)
maxdfdf




def plot_max_df(maxdf):
    ax = maxdf.plot.bar(rot=90,x='Name', y='Rating', figsize=(10,5))
    ax.set_ylim([3.99,5])
    ax1 = maxdf.plot.bar(rot=90,x='Name', y='Reviews', figsize=(10,5))
    return ax, ax1






def max_occurences(df):
    #Hvilket land har haft den bedste vin flest gange.
    no_of_occur_max = df['Country'].value_counts()
    return no_of_occur_max
max_occurences(maxdfdf)