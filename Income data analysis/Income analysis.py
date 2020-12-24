#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv("Income.csv")
df.head()


# In[55]:


df.shape
df.info()


# In[7]:



df.describe()


# In[11]:


# checking for null value 

df.isnull().sum()


# In[12]:


# checking for null value using heat map
sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis") 


# In[44]:


import matplotlib.pyplot as plt
sns.set(style="white", palette="muted", color_codes=True)
f, axes = plt.subplots(3, 2, figsize=(10,10), sharex=True)
sns.despine(left=True)
sns.set(style="whitegrid")
sns.boxplot(x= "WorkingHoursWife"  ,data = df,linewidth=2.5,ax =axes[0,0])
sns.boxplot(x= "WifeAge"  ,data = df,linewidth=2.5,ax =axes[0,1])
sns.boxplot(x= "EducationWife"  ,data = df,linewidth=2.5,ax =axes[1,0])
sns.boxplot(x= "WifeHourEarnings"  ,data = df,linewidth=2.5,ax =axes[1,1])
sns.boxplot(x= "WifeWage"  ,data = df,linewidth=2.5,ax =axes[2,0])




# In[42]:


df.head(1)


# In[46]:


import matplotlib.pyplot as plt
sns.set(style="white", palette="muted", color_codes=True)
f, axes = plt.subplots(2, 2, figsize=(10,10), sharex=True)
sns.despine(left=True)
sns.set(style="whitegrid")
sns.boxplot(x= "WorkingHoursHusband"  ,data = df,linewidth=2.5,ax =axes[0,0])
sns.boxplot(x= "HusbandAge"  ,data = df,linewidth=2.5,ax =axes[0,1])
sns.boxplot(x= "EducationHusband"  ,data = df,linewidth=2.5,ax =axes[1,0])
sns.boxplot(x= "HusbandWage"  ,data = df,linewidth=2.5,ax =axes[1,1])


# In[ ]:





# In[30]:


df.head(1)


# In[39]:


import matplotlib.pyplot as plt
sns.set(style="white", palette="muted", color_codes=True)
f, axes = plt.subplots(2, 2, figsize=(10,10), sharex=True)
sns.despine(left=True)
sns.distplot(df["WorkingHoursWife"],ax=axes[0, 0])
sns.distplot(df["EducationWife"],ax=axes[0, 1])
sns.distplot(df["WifeHourEarnings"], ax=axes[1, 0])
sns.distplot(df["WifeWage"],ax=axes[1, 1])


# In[47]:


import matplotlib.pyplot as plt
sns.set(style="white", palette="muted", color_codes=True)
f, axes = plt.subplots(2, 2, figsize=(10,10), sharex=True)
sns.despine(left=True)
sns.distplot(df["WorkingHoursHusband"],ax=axes[0, 0])
sns.distplot(df["EducationHusband"],ax=axes[0, 1])
sns.distplot(df["HusbandWage"], ax=axes[1, 0])
sns.distplot(df["HusbandAge"],ax=axes[1, 1])


# In[69]:


#Multipile Linear regression

import matplotlib.pyplot as plt
import statsmodels.api as sm
x = df[['WorkingHoursWife','WifeAge','EducationWife','WifeHourEarnings','WifeWage','WorkingHoursHusband','HusbandAge','EducationHusband','HusbandWage','EducationWifeMother','EducationWifeFather','UnemploymentRate','WifeExperience']]
y = df['FamilyIncome']
x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
est.summary()


# In[83]:


#PCA 

#Standardize the Data

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
features = ['WorkingHoursWife','WifeAge','EducationWife','WifeHourEarnings','WifeWage','WorkingHoursHusband','HusbandAge','EducationHusband','HusbandWage','EducationWifeMother','EducationWifeFather','UnemploymentRate','WifeExperience']

# Separating out the features
x = df.loc[:, features].values

# Separating out the target
y = df.loc[:,['FamilyIncome']].values

# Standardizing the features
x = StandardScaler().fit_transform(x)


# In[86]:


#PCA Projection to 2D

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['FamilyIncome']]], axis = 1)
finalDf.head(2)


# In[87]:


#Explained Variance

pca.explained_variance_ratio_


# In[82]:


# Plotting PCA Figure
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
FamilyIncome = [FamilyIncome]
indicesToKeep = finalDf['FamilyIncome'] == FamilyIncome
ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], s = 50)
ax.legend(targets)
ax.grid()


# In[ ]:





# In[ ]:




