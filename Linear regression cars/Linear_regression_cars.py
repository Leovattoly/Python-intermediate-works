#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

data = pd.read_csv("auto.csv")
data.head(3)


# In[6]:


data.isnull().sum()


# In[7]:


sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")


# In[36]:


data.drop(['horsepower'],axis=1,inplace=True)


# In[37]:


data.shape


# In[38]:


type(data['displacement'])


# In[39]:


from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(data,test_size = 0.1,random_state = 0)


# In[40]:


print(train_data)


# In[41]:


model = LinearRegression()


# In[42]:


##setting mpg as target value 
x_train = data.iloc[:,1:10].values
y_train = data.iloc[:,0].values
x_test = data.iloc[:,1:10].values
y_test = data.iloc[:,0].values


# In[49]:


print(y_train)


# In[50]:


model.fit(x_train, y_train)


# In[51]:


r_sq = model.score(x_train, y_train)
print('coefficient of determination:', r_sq)


# ## Intercept of the model

# In[52]:


print('intercept:', model.intercept_)


# ## Slope of the Model

# In[53]:


print('slope:', model.coef_)


# In[54]:


y_pred = model.predict(x_test)


# In[55]:


df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df


# In[60]:


## Ridge Training
from sklearn.linear_model import Ridge

# Alpha value is 0.01
clf = Ridge(alpha=0.01)
clf.fit(x_train, y_train)


# In[66]:


y_pred = clf.predict(x_test)


# In[74]:


score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[75]:


# Alpha value is 0.1
clf = Ridge(alpha=0.1)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[76]:


# Alpha value is 1
clf = Ridge(alpha=1)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[82]:


# Alpha value is 10
clf = Ridge(alpha=10)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[113]:


df_ridge = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df_ridge


# In[80]:


from sklearn.linear_model import Lasso
lasso_model = Lasso(alpha=0.01)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[81]:


# Alpha value is 0.1
lasso_model = Lasso(alpha=0.1)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[83]:


# Alpha value is 1
lasso_model = Lasso(alpha=1)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[84]:


# Alpha value is 10
lasso_model = Lasso(alpha=10)
clf.fit(x_train, y_train)
score_r2 = clf.score(x_test,y_test) 
print("R^2 score :", score_r2*100)


# In[89]:


from sklearn.neighbors import KNeighborsRegressor
kneigh = KNeighborsRegressor(n_neighbors=5)
data_kregression = pd.read_csv("auto.csv")

data_kregression.drop(['cylinders','displacement','weight','acceleration','model year','origin','car name'],axis=1,inplace=True)


# In[91]:


data_kregression.drop(['mpg'],axis=1,inplace=True)


# In[92]:


train_data,test_data = train_test_split(data_kregression,test_size = 0.1,random_state = 0)


# In[93]:


data_kregression.head()


# In[95]:


kneigh.fit(x_train,y_train)


# In[112]:


y_pred = kneigh.predict(x_test)


# In[114]:


df_kneigh = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df_kneigh


# In[116]:


score_r2 = kneigh.score(x_test,y_test)
print("R^2 value : ",score_r2*100)


# In[ ]:





# In[ ]:




