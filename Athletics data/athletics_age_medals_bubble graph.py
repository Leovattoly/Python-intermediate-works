#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

athletes_data = pd.read_csv("athletes.csv")

athletes_data.head()


# In[40]:


x_ath = athletes_data[athletes_data['sport'] == "athletics" ]
x_volley = athletes_data[athletes_data['sport'] == "volleyball" ]
x_shooting = athletes_data[athletes_data['sport'] == "shooting " ]

X = pd.concat([x_ath, x_volley,x_shooting], axis=0)


medals = athletes_data['gold']+athletes_data['silver']+athletes_data['bronze']




athletes_data['Date'] = pd.to_datetime(athletes_data.dob)
athletes_data['Date']


athletes_data.head()


# In[45]:


def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

y = athletes_data['Date'].apply(lambda x: from_dob_to_age(x))
print(y)


# In[48]:


medals = medals.values.tolist()
y = y.values.tolist()
print(medals)
print(y)


# In[52]:


plt.scatter(medals, y)
plt.show()


# In[ ]:




