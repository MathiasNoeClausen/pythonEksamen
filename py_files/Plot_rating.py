#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
import seaborn as sns


# In[2]:


def scroll(driver, timeout, loops):
    scroll_pause_time = timeout

    last_height = driver.execute_script("return document.body.scrollHeight")
    num = 0
    
    while True and num < loops:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        num = num + 1
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# In[4]:


url = 'https://www.vivino.com/explore?e=eJwdijsOgCAQBW_zaqDfzo4jGGPWFQmJgAH83V5iM1PMxEIaMSRSiPyQ0UpBXhospMPi6NlvdHEJrvGOvFDhFpKvs-QzNWRaXRXcbZz6-st8itQcHw%3D%3D'
product_names = []
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
browser.get(url)

loops = 1
timeout = 5
scroll(browser, timeout, loops)

titles = browser.find_elements_by_class_name('vintageTitle__wine--U7t9G')
prices = browser.find_elements_by_xpath("(//*[contains(@class, 'addToCartButton__price')])")
ratings = browser.find_elements_by_class_name('vivinoRating__averageValue--3Navj')
reviews = browser.find_elements_by_class_name('vivinoRating__caption--3tZeS')
countries = browser.find_elements_by_xpath('//a[contains(@href, "/explore?country_code")]')
#for price in prices:
#    print('price:',price.text)
for title, price, rating, review, country in zip(titles, prices, ratings, reviews, countries):
    with open('vinData.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        date = 9999
        line = re.findall(r'\d+', title.text)
        
        if(len(line)>0):
            for l in line:
                if(len(str(l)) == 4):
                    date = l
                    
        data = [title.text, date, price.text.split("\n", 1)[0], rating.text, review.text.split(" ", 1)[0], country.text]
        writer.writerow(data)
                                


# In[3]:


df = pd.read_csv('vinData.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
df.head()


# In[4]:


df.describe()


# In[5]:


sorted_df = df.copy()
sorted_df.drop(sorted_df[df.Review < 1500].index, inplace=True)
print(sorted_df)


# In[54]:


def plot_rating(df):
    
    all_lowest = df.loc[df['Rating'] == df['Rating'].min()]
    print('Lowest rated:',all_lowest[:3],'\n')
    #print('Median rating',df.mean(),'\n')
    
    all_highest = df.loc[df['Rating'] == df['Rating'].max()]
    print('Highest rated:',all_highest[:3])
    
    #Delete all with low review numbers
    sorted_df = df.copy()
    #sorted_df.drop(sorted_df[df.Review < 1500].index, inplace=True)
    
    #Extract Country & Rating columns
    cols = ['Country', 'Rating']
    mask = sorted_df[cols]
    
    #Group rows by Country
    mask_by_country = mask.groupby('Country')
    
    #Get Min, Median & Max rating for each country
    min_rating = mask_by_country.min()
    median_rating = mask_by_country.mean()
    max_rating = mask_by_country.max()
    
    df_stats = pd.DataFrame()
    df_stats['Min'] = min_rating['Rating']
    df_stats['Median'] = median_rating['Rating']
    df_stats['Max'] = max_rating['Rating']
    ax = df_stats.plot(kind='bar', figsize=(15,10), width=0.7)
    plt.xticks(rotation=45)
    plt.xlabel('Country')
    plt.ylabel('Rating pr. country');
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3)
    
    #Data on each bar
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, (p.get_height()) * 1.005), rotation=90)
    
def describe(df):
    return df.describe()

plotbar = df.copy()
plot_rating(plotbar)


# In[41]:


cols = ['Country', 'Rating']
mask = df[cols]
mask.info()
mask


# In[57]:


def describe_df(mask):
    mask_by_country = mask.groupby('Country')
    print(type(mask_by_country))
    return mask_by_country.describe()
describe_df(mask)


# In[43]:

mask_by_country = mask.groupby('Country')
min_rating = mask_by_country.min()
median_rating = mask_by_country.mean()
max_rating = mask_by_country.max()
median_rating


# In[44]:


newdf = pd.DataFrame()
newdf['Min'] = min_rating['Rating']
newdf['Median'] = median_rating['Rating']
newdf['Max'] = max_rating['Rating']
newdf.plot(kind='bar', figsize=(10,5))
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)

mydata = [min_rating['Rating'], median_rating['Rating'], max_rating['Rating']]
headers = ['Min', ['Median'], ['Max']]
newdf = pd.DataFrame(mydata, headers)
newdf.plot(kind='bar', figsize=(10,5))
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1)


# In[46]:


median_rating.idxmax()


# In[77]:


plt.plot(median_rating.index, median_rating)
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('Average rating pr. country');


# In[80]:

def plot_red(red_df):
    #red_df = pd.read_csv('redwinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
    red_df.drop(red_df[red_df.Review < 112].index, inplace=False)
    return plot_rating(red_df)
red_df = pd.read_csv('redwinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
plot_red(red_df)


# In[82]:


def plot_white(white_df):
    #white_df = pd.read_csv('whitewinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
    white_df.drop(white_df[white_df.Review < 65].index, inplace=False)
    return plot_rating(white_df)
white_df = pd.read_csv('whitewinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
plot_white(white_df)


# In[83]:


def plot_sparkling(sparkling_df):
    #sparkling_df = pd.read_csv('sparklingwinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
    sparkling_df.drop(sparkling_df[sparkling_df.Review < 95].index, inplace=False)
    return plot_rating(sparkling_df)
sparkling_df = pd.read_csv('sparklingwinedata.csv', names=["Name", "Year", "Price", "Rating", "Review", "Country"])
plot_sparkling(sparkling_df)

