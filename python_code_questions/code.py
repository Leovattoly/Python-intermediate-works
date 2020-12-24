#!/usr/bin/env python
# coding: utf-8

# In[7]:


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:58:39 2020
"""
import numpy as np 
import pandas as pd 
from scipy.stats import beta, truncnorm 
import seaborn as sns 
import matplotlib.pyplot as plt 

np.random.seed(0) 
df = pd.DataFrame(columns=['leverage', 'debt beta', 'equity beta']) 
df['leverage'] = beta.rvs(1, 3, scale = 1.75, size = 1000)/2 
df['debt beta'] = truncnorm.rvs(.05, .07, size = 1000) + df['leverage']*0.0001 
df['equity beta'] = np.random.normal(1, 0.25, size = 1000) 
# print(df['leverage'] )

# Question 1

from scipy.stats import skew 
import pylab as p  
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(df['leverage'])**2  ) 
p.plot(df['leverage'], y1, '*') 
print( '\nSkewness for data : ', skew(df['leverage']))   


# In[8]:


# question 2

df.hist(column='leverage')


# In[ ]:




