# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:55:09 2020

@author: DELL
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys

# inserting data 
df = pd.read_csv("data.csv")
# print(df.head())

# Get the unique values of 'B' column 
unique_jobs = df.job.unique() 
# print(unique_jobs)
profession = str(sys.argv[1])
# Checking if profession exists in unique_jobs  
# using in 
if (profession in unique_jobs): 
    print ("Profession exists in unique job list") 
else:
    print ("Profession not exists in unique job list") 

      