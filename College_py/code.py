#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import seaborn as sns


#1.Load the data from "college.csv" that has attributes collected about private and public colleges for a particular year.  
# We will try to predict the private/public status of the college from other attributes.

df = pd.read_csv("College.csv")
df.head()


# In[20]:


# Removing the non-numeric value and replacing with 0 or 1.Instead of private new column Yes

private_public = pd.get_dummies(df['Private'],drop_first=True) # 0 for false
private_public.head(1)
df = pd.concat([df,private_public],axis=1)


# In[21]:





# In[22]:


df.head(1)


# In[24]:


# dropping the private column

df.drop(['Private'],axis=1,inplace=True)


# In[25]:


df.head(1)


# In[29]:


# 2.Use LabelEncoder to encode the target variable in to numerical form 
# split the data such that 20% of the data is set aside for testing.

from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(df,test_size = 0.2,random_state = 100)

train_data.shape


# In[33]:


# splitting data nto features and outpu

x_train = train_data.iloc[:,1:17].values
y_train = train_data.iloc[:,17].values


# In[34]:


# initializing the Linear SVC model

from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
clf = make_pipeline(StandardScaler(),LinearSVC(random_state=0, tol=1e-5))


# In[35]:


# training the model

clf.fit(x_train, y_train)


# In[36]:


# testing the model

x_test = test_data.iloc[:,1:17].values
y_predicted = clf.predict(x_test)


# In[37]:


print(y_predicted)


# In[38]:


y_test = test_data.iloc[:,17].values


# In[50]:





# In[56]:


df_prediction = pd.DataFrame(y_test,columns = ['Real_value '])


# In[57]:


df_prediction ['Predicted_values'] = y_predicted


# In[58]:


# showing the predicted and real values

df_prediction.head(5)


# In[ ]:




