# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:33:05 2020

@author: DELL
"""

import matplotlib.pyplot as plt
import pandas as pd


# inserting data 
df = pd.read_csv("crime.csv",encoding='latin-1')
#print(df.head())
# Fill in nans in SHOOTING column
df.SHOOTING.fillna('N', inplace=True)
# How many crimes were reported in the year 2015? 
df_2015 = df.loc[df['YEAR'].isin([2015])]
print("Number of crimes in 2015: ",len(df_2015))

# 2. How many incidents involving shootings were reported in the year 2018? 
df_2018= df.loc[df['YEAR'].isin([2018])]
df_2018= df.loc[df['SHOOTING'].isin([])]
print("Number of shooting in 2018: ",len(df_2018))

# 3. How many "larceny" incidents occurred in 2017? 
df_2017 = df.loc[df['YEAR'].isin([2017])]
df_2017 = df_2017.loc[df_2017['OFFENSE_CODE_GROUP'].isin(['Larceny'])]
print("Number of larceny incidents occurred in 2017: ",len(df_2017))

# 4. How many "drug violation" incidents occurred in all Districts "A" and "B" combined? 
df_drug = df.loc[df['OFFENSE_CODE_GROUP'].isin(['Drug Violation'])]
df_drug = df_drug.loc[df['DISTRICT'].isin(['A' and 'B'])]
print("Number of drug violation  incidents occurred in : ",len(df_drug))

import seaborn as sns
# Countplot for crime types
sns.catplot(y='OFFENSE_CODE_GROUP',
           kind='count',
            height=8, 
            aspect=1.5,
            order=df.OFFENSE_CODE_GROUP.value_counts().index,
           data=df)

# 5. Which were the three most common offense codes in 2016 (sorted in descending order of the number of offenses)? 

sns.scatterplot(x='Lat',
               y='Long',
                alpha=0.01,
               data=df)