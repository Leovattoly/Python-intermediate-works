#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Use np.loadtxt(...) to load the data into Spyder

import numpy as np

df = np.loadtxt("data.txt") 


# In[8]:


# 2- Make a histogram of the length of all the notes (hint: Use X[:,0]). Comment on the distribution.

import matplotlib.pyplot as plt

plt.hist(df[:,0])
plt.show()


# In[23]:


# 3- Make a boxplot of the distance of the inner frame to the upper border. 
# Are there any points that look like outliers? Which point(s)?

import pandas as pd

green_diamond = dict(markerfacecolor='g', marker='D')
x = pd.DataFrame(df,columns=['Col1', 'Col2', 'Col3', 'Col4','Col5','Col6'])

fig1, ax1 = plt.subplots()
boxplot = x.boxplot(column=['Col1'],flierprops=green_diamond)

fig2, ax2 = plt.subplots()
boxplot = x.boxplot(column=['Col2'],flierprops=green_diamond)

fig3, ax3 = plt.subplots()
boxplot = x.boxplot(column=['Col3'],flierprops=green_diamond)

fig4, ax4 = plt.subplots()
boxplot = x.boxplot(column=['Col4'],flierprops=green_diamond)

fig5, ax5 = plt.subplots()
boxplot = x.boxplot(column=['Col5'],flierprops=green_diamond)

fig6, ax6 = plt.subplots()
boxplot = x.boxplot(column=['Col6'],flierprops=green_diamond)


# In[24]:


# 4- Perform a principal component analysis (PCA) projection from the 6 dimensions to 2 dimensions. 
# Do not plot. (Comment: Usually, before doing a PCA projection, you should scale the data, 
# by subtracting the mean and dividing by the standard deviation. In this project, we will not do this, 
# for the sake of simplicity, and because the variables are not extremely different in terms of their scale.) 

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
    
pca.fit(x)


# In[25]:


principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])


# In[29]:





# In[ ]:




