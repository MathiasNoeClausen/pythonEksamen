## **WEBSCRAPING AND ANALYSIS OF WINES ON VIVINO.COM**

I dette projekt vil vi scrape de forskellige oplysninger der findes om vine fra vivino.com.
Det skal så analyseres på bl.a. rating, antal reviews, pris og smagsnoter, så vi kan bestemme fx. hvilken vin der var højest rated i 2009 og om der er en correlation mellem smagsnoter og pris.



## **USER GUIDE**

Alle metoder der bliver brugt til at hente, analysere og illustrere data ligger i mappen 'Project_Main'. Burde bare kunne køres og så henter den selv fra py filerne.



## **USED TECHNOLOGIES**
```
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options

from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import MeanShift, estimate_bandwidth

from sklearn.model_selection import train_test_split

from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import csv

import re

import time

import seaborn as sns
```

## **STATUS:**
Vi kom igennem med det opgaver, vi havde sat os ud for. Det eneste som vi ikke nåede at implementere var en machine learning funktion der blev trænet på f.eks. smagsnoter, lande, mængden af reviews osv. til bedre at kunne predicte en vins pris.


## **Metoder til at analysere vin:**
Webscraping metoder i folderne Scrape_Data og Scrape_With_notes

plot_rating (Laver en graf som viser min, median og max rating på de forskellige lande, samt information om de 1-3 lavest og højest rated vine)

describe_df (Beskriver hvor mange vine der er fra de enkelte lande samt data på rating.)

max_rating_df (Finder de bedste vine for hvert år, og laver et nyt dataframe ud fra det.)

plot_max_df (Tager det nye dataframe fra max_rating_df og laver to grafer, en der viser højeste rating på vin for hvert år og en der viser reviews på de samme vin)

max_occurences (Viser hvor mange gange hvert land har haft den bedste vin)

get_distribution_of_ratings (Viser en graf over fordelingen af ratings)

get_correlation (Viser korrelationen mellem pris, ratings og år)

plot_price_and_rating_correlation (Lavet et plot med regression på pris og rating)

plot_year_and_rating_correlation (Gør det ovenstående men for år og rating)

improvement_in_correlation_over_time (Tester om vi har scraped nok data til at danne os et præcist billede)

predict_prices (Bruger sklearn LinearRegression til at gætte prisen)

create_3d_plot (Laver en 3d præsentation af vor vine placeres efter deres kraftighed, sødme og syre, farvet efter hvilken type af vin det er)

create_predicted_3d_plot (Forsøger at lave en opdeling og 3d præsentation af de samme vin alt efter, hvordan de clusters. Her bruges MeanShift)

plot_mean_notes_for_countries (Laver en graf over den gennemsnitlige kraftighed, sødme og syre afhængigt af hvilket land de kommer fra)

get_correlation_between_country_and_notes (Navngivet lidt forkert men kigger på lande, deres temperatur, og hvilken indflydelse det har på smagsnoterne)

plot_mean_notes_for_winetypes (Laver en lignende graf men denne gang opdelt efter vintyper)
