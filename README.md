Wine analysis exam project

I dette projekt vil vi scrape de forskellige oplysninger der findes om vine fra vivino.com.
Det skal så analyseres på bl.a. rating, antal reviews, pris og smagsnoter, så vi kan bestemme fx. hvilken vin der var højest rated i 2009.

USED TECHNOLOGIES

NEED TO IMPORT:
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

I dette program findes der følgende metoder til at analysere vin:

plot_rating (Laver en graf som viser min, median og max rating på de forskellige lande, samt information om de 1-3 lavest og højest rated vine)
describe_df (Beskriver hvor mange vine der er fra de enkelte lande samt data på rating.)

Viser grafer for de forskellige typer vin:
red_df,
white_df, 
sparkling_df


STATUS:
1. Vi vil forudsige kvaliteten af vine ud fra de oplysninger vi kan finde på den enkelte vin
på vivino.com DONE
2. Vi vil se om der er en sammenhæng mellem pris og anmeldelsen på vinen. DONE
3. Vise en graf over lande med bedst rating. DONE
4. Har årstal og rating en sammenhæng. DONE
5. Hvilket land kan man købe bedst billig vin i.
6. Hvilken type vin har været mest populær i de givne år. DONE
7. (ikke lav denne) Vi vil kunne anbefale vine alt efter hvilke smagsnoter man ønsker.
8. måske et eller andet scoring/vægt system der sammenligner pris og ratings for at give dem med højest score
9. machine learning clustering
