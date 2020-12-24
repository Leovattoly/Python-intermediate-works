#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
titanic_data = pd.read_csv("titanic_train.csv")
titanic_data.head(3)


# In[17]:


titanic_data.drop("Cabin",axis = 1,inplace=True)


# In[18]:


sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap="viridis")


# In[19]:


titanic_data.isnull().sum()


# In[20]:


titanic_data.dropna(inplace=True)


# In[21]:


titanic_data.isnull().sum()


# In[22]:


sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap="viridis")


# In[23]:


sex = pd.get_dummies(titanic_data['Sex'],drop_first=True) # 0 for false
sex.head(5)


# In[24]:


embark = pd.get_dummies(titanic_data['Embarked'], drop_first=True)
pcls = pd.get_dummies(titanic_data['Pclass'], drop_first=True)


# In[25]:


titanic_data = pd.concat([titanic_data,sex,embark,pcls],axis=1)
titanic_data.head(3)


# In[26]:


titanic_data.drop(['PassengerId','Pclass','Name','Sex','Ticket','Embarked'],axis=1,inplace=True)


# In[27]:


titanic_data.head(3)


# In[67]:


from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(titanic_data,test_size = 0.1,random_state = 100)
#sel = sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from numpy import set_printoptions


# In[76]:


x_train = train_data.iloc[:,1:10].values
y_train = train_data.iloc[:,0].values
# feature extraction
test = SelectKBest(score_func=f_classif, k=2)
fit = test.fit(x_train, y_train)
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x_train)
# summarize selected features
print(features[0:5,:])
#sel.fit_transform(x_train)
#print(x_train)
x_test = test_data.iloc[:,1:10].values
y_test = test_data.iloc[:,0].values


# In[77]:


from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state = 1)
classifier.fit(features,y_train)


# In[78]:


y_pred = classifier.predict(x_test)


# In[72]:


test_data["Predictions"] = y_pred


# In[73]:


test_data.head(5)


# In[74]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
accuracy = float(cm.diagonal().sum())/len(y_test)
print("\nAccuracy Of SVM For The Given Dataset : ", accuracy)


# In[36]:


titanic_data.shape


# In[ ]:





# In[ ]:




