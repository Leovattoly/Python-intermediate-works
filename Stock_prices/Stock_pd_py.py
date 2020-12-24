#!/usr/bin/env python
# coding: utf-8

# In[8]:


# inserting data 
import pandas as pd
amazon_df = pd.read_csv("amazon.csv",parse_dates =["Date"], index_col ="Date")
ibm_df = pd.read_csv("ibm.csv",parse_dates =["Date"], index_col ="Date")
fb_df = pd.read_csv("fb.csv",parse_dates =["Date"], index_col ="Date")
mmm_df = pd.read_csv("mmm.csv",parse_dates =["Date"], index_col ="Date")
fb_df.head()


# In[30]:


# checking for any NA values

import seaborn as sns

sns.heatmap(ibm_df.isnull(),yticklabels=False,cmap="viridis")
sns.heatmap(amazon_df.isnull(),yticklabels=False,cmap="viridis")
sns.heatmap(fb_df.isnull(),yticklabels=False,cmap="viridis")
sns.heatmap(mmm_df.isnull(),yticklabels=False,cmap="viridis")


# In[10]:


# Resampling the time series data based on months 
# we apply it on stock close price 
# 'M' indicates month 
amazon_monthly_resampled_data = amazon_df.AdjClose.resample('M').mean() 
# print(amazon_monthly_resampled_data)
ibm_monthly_resampled_data = ibm_df.AdjClose.resample('M').mean() 
fb_monthly_resampled_data = fb_df.AdjClose.resample('M').mean() 
mmm_monthly_resampled_data = mmm_df.AdjClose.resample('M').mean() 
# print(mmm_monthly_resampled_data)


# In[25]:


import matplotlib.pyplot as plt

pd.plotting.autocorrelation_plot(amazon_monthly_resampled_data)
plt.title('Autocorrelation of the adjusted month-end close prices of Amazon stock')


# In[26]:


pd.plotting.autocorrelation_plot(ibm_monthly_resampled_data)
plt.title('Autocorrelation of the adjusted month-end close prices of IBM stock')


# In[27]:


pd.plotting.autocorrelation_plot(fb_monthly_resampled_data)
plt.title('Autocorrelation of the adjusted month-end close prices of FB stock')


# In[28]:


pd.plotting.autocorrelation_plot(mmm_monthly_resampled_data)
plt.title('Autocorrelation of the adjusted month-end close prices of MMM stock')


# In[ ]:




