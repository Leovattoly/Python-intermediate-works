#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv("SalaryGender.csv")
df.head()


# In[2]:


# converting each column to NumPy Array

salary = np.array(df['Salary'])
Gender = np.array(df['Gender'])
Age = np.array(df['Age'])
PhD = np.array(df['PhD'])


# In[11]:


# 1. The number of men with a PhD
# 2. The number of women with a PhD

number_of_women_with_phd = 0
number_of_men_with_phd = 0

for i in range(len(PhD)):
    if PhD[i] == True and  Gender[i]== True:
        number_of_men_with_phd = number_of_men_with_phd +1
    elif PhD[i] == True and  Gender[i]== False:
            number_of_women_with_phd = number_of_women_with_phd +1
            
print("Number of men with a PhD: ",number_of_men_with_phd)
print("\nNumber of women with a PhD: ",number_of_women_with_phd)


# In[29]:


# Store the "Age" and "PhD" columns in one DataFrame
# and delete the data of all people who don't have a PhD

df = pd.read_csv("SalaryGender.csv")

df_new = df [(df[['PhD']] != 0).all (axis = 1)]
# print(df_new)

df_new = df_new[['Age','PhD']]

df_new.head()


# In[35]:


# Calculate the total number of people who have a PhD degree
   
no_of_Phd = len(df_new)
print("number of people who have a PhD degree: ",no_of_Phd)


# In[ ]:




