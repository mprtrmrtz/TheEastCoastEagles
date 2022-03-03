# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:02:34 2022

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


COVID_Hospitals= pd.read_csv("Data/COVID_Data/data/context_hospitals_covidcaremap-2021-05-29.csv")

df = COVID_Hospitals
df.head()



df['FIPS'] = df['Name']

start = 0
end = df.shape[0]//5
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']
    
start = df.shape[0]//5
end = (df.shape[0]//5) * 2
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']

start = (df.shape[0]//5) * 2
end = (df.shape[0]//5) * 3
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']
    
start = (df.shape[0]//5) * 3
end = (df.shape[0]//5) * 4
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']
    
    
start = (df.shape[0]//5) * 4
end = (df.shape[0]//5) * 5
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']    
    
    
start = (df.shape[0]//5) * 5
end = df.shape[0] 
for i in range(start, end):
    params = []
    url = []
    response = []
    params = urllib.parse.urlencode({'latitude': df['Latitude'].iloc[i,], 'longitude': df['Longitude'].iloc[i,], 'format':'json'})
    url = 'https://geo.fcc.gov/api/census/block/find?'  + params 
    response =  requests.get(url)
    data = response.json()
    df['FIPS'].iloc[i,] = data['County']['FIPS']  
    


df['FIPS'].tail()


df.to_csv('COVID_Hospitals_PYTHON.csv')





































































































