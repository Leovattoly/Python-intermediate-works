#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from matplotlib import pyplot as plt 
import pandas as pd


# inserting data 
df = pd.read_csv("jaccard_output.txt")
df.head()

# Creating histogram 
fig, ax = plt.subplots(figsize =(10, 10)) 
ax.hist(df["Score"], bins = [0.0,0.005,0.0075,0.01]) 
  
# Show plot 
plt.show() 

