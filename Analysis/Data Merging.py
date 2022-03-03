# -*- coding: utf-8 -*-
"""
Created on Fri May 28 03:26:52 2021

@author: momaleki
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce


os.chdir("C:/Users/momaleki/Desktop/Project/Data/ToMerge")
print(os.getcwd())

space = "\n"


#%% Importing datasets

# SCI = pd.read_csv("SCI.csv")
mask = pd.read_csv("mask_use.csv")
FIPS = pd.read_csv('FIPS_master.csv')
Education = pd.read_csv('Education_level.csv')
Election = pd.read_csv('Election_decisions.csv')
longlat = pd.read_csv('FIPS_to_longlat.csv')
Unemployment = pd.read_csv('Unemployment.csv')
movement = pd.read_csv('movement_range.csv')
Rural = pd.read_csv('Rural_percentage.csv')
Population = pd.read_csv('Population_density.csv')
Poverty = pd.read_csv('Poverty_estimate.csv')
confirmed = pd.read_csv('COVID_confirmed_cases.csv')
death = pd.read_csv('COVID_death_cases.csv')
essential = pd.read_csv('COVID_essential_workers.csv')
hospital = pd.read_csv('COVID_hospital_locations.csv')
capacity = pd.read_csv('COVID_testing_capacity.csv')
counts = pd.read_csv('COVID_testing_counts.csv')
clinics = pd.read_csv('COVID_testing_clinics.csv')
Crime = pd.read_csv('Crime.csv')
Vaccine = pd.read_csv('Vaccine.csv')
Vaccine_test = pd.read_csv('Vaccine_test.csv')
Investment = pd.read_csv('Fed_Investment.csv')



#%% Data Processing NO Federal Investment

dataset_list = [mask, FIPS, Education, Election, longlat, Unemployment, movement, Rural, Population, 
                Poverty, confirmed, death, 
                essential, hospital, capacity, counts, clinics, Vaccine, Crime, Vaccine_test]

for dataset in dataset_list:
    if "Unnamed: 0" in dataset.columns:
        del dataset["Unnamed: 0"]
        print(space)
        print(dataset.head())

df_final_no_federal = reduce(lambda left,right: pd.merge(left,right, on='FIPS'), dataset_list)

#%% Data Processing WITH Federal Investment


dataset_list = [mask, FIPS, Education, Election, longlat, Unemployment, movement, Rural, Population, 
                Poverty, confirmed, death, 
                essential, hospital, capacity, counts, clinics, Vaccine, Crime, Vaccine_test, 
                Investment]

for dataset in dataset_list:
    if "Unnamed: 0" in dataset.columns:
        del dataset["Unnamed: 0"]
        print(space)
        print(dataset.head())

df_final_with_federal = reduce(lambda left,right: pd.merge(left,right, on='FIPS'), dataset_list)

#%%

df_final_no_federal.to_csv('df_no_Federal.csv')
df_final_with_federal.to_csv('df_with_Federal.csv')






































































