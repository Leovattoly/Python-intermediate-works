#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd

# inserting data 
df = pd.read_csv("roman-emperor-reigns.csv")
df.head()


# 

# In[5]:


df1 = df[df['Cause_of_Death'] == "Assassinated" ]
df1.head()


# In[15]:


fig= plt.figure(figsize=(9,9))
# Plot
patches, texts = plt.pie(df1.Length_of_Reign, shadow=True, startangle=90)
plt.legend(df1.Emperor, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[ ]:




