#!/usr/bin/env python
# coding: utf-8

# In[25]:


# i).Load the data from "glass.csv" and make a bar plot of different types of glasses.

# inserting data 
import pandas as pd
df = pd.read_csv("glass.csv")
df.head()
df.shape


# In[22]:


df.plot(y = ["RI","Na","Mg","Si","K","Ca","Ba","Fe","Type"],kind = "bar")


# In[39]:


# ii).Make a train_test split and fit a single decision tree classifier.

from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(df,test_size = 0.3,random_state = 1)

x_train = train_data.iloc[:,0:9].values
y_train = train_data.iloc[:,9].values
x_test = train_data.iloc[:,0:9].values
y_test = train_data.iloc[:,9].values
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit (x_train,y_train)
y_predict = clf.predict(x_test)

predicted_test = list(zip(y_test, y_predict))  
predicted_df = pd.DataFrame(predicted_test, columns = ['Actual Values', 'Predicted Values'])  
predicted_df.head(3)


# In[46]:


# iii).Make a k-fold split with 3 splits and measure the accuracy score with each split

from sklearn.model_selection import KFold
kf = KFold(n_splits=3)


# In[ ]:


from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_jobs=-1,max_features= 'sqrt' ,n_estimators=50, oob_score = True) 

param_grid = { 
    'n_estimators': [200, 700],
    'max_features': ['auto', 'sqrt', 'log2']
}

CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5)
CV_rfc.fit(x_train, y_train)
y_predict =  CV_rfc.predict(x_test)
CV_rfc.best_params_
best_grid = CV_rfc.best_estimator_

print("Acuracy of Random Forest Classifier:",CV_rfc.score(y_test,y_predict))


# In[ ]:




