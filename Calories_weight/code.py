#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!usrbinenv python
# coding utf-8

# In[2]


# inserting data 
import pandas as pd
df = pd.read_csv("data_calories.csv")
df.head(3)


# In[4]







# In[3]:


X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 13, random_state = 0)


# In[5]




# In[4]:


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[6]


# Predicting the Test set results
y_pred = regressor.predict(X_test)


# In[9]



# In[10]:


# Visualising the Training set results

import matplotlib.pyplot as plt
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Weight gained gram vs Consumed calories(Training set)')
plt.xlabel('Weight gained gram ')
plt.ylabel('Consumed calories')
plt.show()



# In[11]:


# In[10]



# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Weight gained gram vs Consumed calories(Test set)')
plt.xlabel('Weight gained gram ')
plt.ylabel('Consumed calories')
plt.show()


# In[12]


# R ^2 value of the linear regression model

from sklearn.metrics import r2_score

r_value = r2_score(y_test, y_pred,multioutput='variance_weighted')
print( "R^2 value for the model prepared" ,r_value)


# In[ ]


# In[ ]:




