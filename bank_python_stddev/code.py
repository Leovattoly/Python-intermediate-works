import pandas as pd

import seaborn as sns

import numpy as np

import scipy.stats as st


import matplotlib.pyplot as plt

#import the data

df = pd.read_csv('bank-full.csv',sep=";")
print(df.head())
df.age.str.split(expand=True)
print(df['age'])