# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:20:11 2020

@author: DELL
"""

import numpy as np

import pandas as pd

from pandas_datareader import data as wb

from scipy.stats import norm

import matplotlib.pyplot as plt

#matplotlib inline

 

ticker = 'PG'

data = pd.DataFrame()

data[ticker] = wb.DataReader(ticker, data_source='yahoo', start = '2007-1-1', end='2017-03-21')['Adj Close']

 

log_returns = np.log(1 + data.pct_change())

 

r = 0.025

 

stdev = log_returns.std() * 250 ** 0.5

 

type(stdev)

 

stdev.values

 

T= 1.0  #Time to Maturity

t_intervals = 250

delta_t = T / t_intervals

 

 

iterations = 1000

 

Z = np.random.standard_normal((t_intervals + 1, iterations))

S = np.zeros_like(Z)

S0 = data.iloc[-1]

 