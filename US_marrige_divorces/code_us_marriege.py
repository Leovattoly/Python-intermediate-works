#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import pandas as pd

# inserting data 
df = pd.read_csv("us-marriages-divorces-1867-2014.csv")
df.head()


# In[22]:


# Data between  1900, 1950, and 2000

df1 = df[df['Year'] >= 1900 ]
df2 = df1[df['Year'] <=2000 ]
df2.head()


# In[26]:


fig= plt.figure(figsize=(10,10))
plt.bar(df2['Marriages_per_1000'],df2['Divorces_per_1000'], label=" number of marriages and divorces per capita ")
plt.legend()

# The following commands add labels to our figure.
plt.xlabel('Marriages')
plt.ylabel('Divorces')
plt.title('Vertical Bar chart')

plt.show()


# In[ ]:




