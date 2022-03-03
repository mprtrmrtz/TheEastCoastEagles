# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 18:54:01 2022

@author: momaleki
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import requests
import urllib


os.chdir("C:/Users/momaleki/Desktop/Project")
os.getcwd()


df = pd.read_csv("Data/IV Regression/merged.csv")

df.head()

df['FIPS'] = df['Recipient']

start = 0
end = df.shape[0]
for i in range(start, end):
    try:
        params = []
        url = []
        response = []
        params = urllib.parse.urlencode({'latitude': df['LAT'].iloc[i,], 'longitude': df['LON'].iloc[i,], 'format':'json'})
        url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
        response =  requests.get(url)
        data = response.json()
        df['FIPS'].iloc[i,] = data['County']['FIPS']

    except KeyError:
        pass    


df.to_csv("merged_FIPS.csv")













































