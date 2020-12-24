#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv("HollywoodMovies.csv")
df.head()


# In[24]:


#1.Find the highest rated movie in the "Quest" story type.

df_quest = df [(df[['Story']] == 'Quest').all (axis = 1)]
df_quest.sort_values(by=['RottenTomatoes'],ascending=False)
highest_rated_movie_quest = df_quest['Movie'].iloc[0]
print("The highest rated movie in the Quest story type: ",highest_rated_movie_quest)


# In[47]:


# 2.Find the genre in which there has been the greatest number of movie releases

df.groupby('Genre')['Movie'].count()


# In[56]:


# 3.Print the names of the top five movies with the costliest budgets.

df_costliest = df.sort_values(by=['Budget'],ascending=False)
costliest_budget_movie = df_costliest['Movie'].iloc[0:5]
print("the top five movies with the costliest budgets: \n",costliest_budget_movie)


# In[66]:


# 4.Is there any correspondence between the critics' evaluation of a movie and its acceptance by the public? 
# Find out, by plotting the net profitability of a movie against the ratings it receives on Rotten Tomatoes.

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x= df["RottenTomatoes"]  ,y =df['Profitability'])


# In[67]:


sns.scatterplot(x= df["RottenTomatoes"]  ,y =df['Profitability'])


# In[ ]:




