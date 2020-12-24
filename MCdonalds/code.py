#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import pandas as pd

# inserting data 
df = pd.read_csv("Mcdonald.csv")

# Plot graphically which food categories have the highest and lowest varieties.

fig = plt.figure(figsize = (15,8)) 
# creating the bar plot 
plt.bar(df['Category'], df['Item'], color ='maroon',width = 0.4) 
plt.xlabel("Category") 
plt.ylabel("Different varieties") 
plt.show() 


# In[ ]:





# In[ ]:





# In[35]:


# Which all variables have an outlier?

col_ = list( df.columns)
g = sns.PairGrid(df, vars=col_)
g.map(plt.scatter, alpha=1)
g.add_legend();


# In[36]:


# Which variables have the highest correlation? Plot them and find out the value

corr = df.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);


# In[50]:


# Which category contributes to the maximum % of Cholesterol in a diet (% daily value)?

column = df[["Category","Cholesterol (% Daily Value)"]]
max_value = column.max()
print("category contributes to the maximum % of Cholesterol in a diet (% daily value): ",list(max_value))


# In[46]:


# Which item contributes maximum to the Sodium intake?

column = df[["Item","Sodium"]]

max_value = column.max()
print("Item contributes maximum to the Sodium intake: ",list(max_value))


# In[57]:


# Which 4 food items contain the most amount of Saturated Fat?

column = df[["Item","Saturated Fat"]]

four_items = column.sort_values(by=['Saturated Fat'],ascending=False)
print("4 food items contain the most amount of Saturated Fat:\n",four_items[0:5])


# In[ ]:




