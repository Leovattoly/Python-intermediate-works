#!/usr/bin/env python
# coding: utf-8

# In[3]:


# i).Use the dataset -digits. Make a 80-20 train/test split.

# importing digit dataset
from sklearn.datasets import load_digits
digits = load_digits()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

#  Make a 80-20 train/test split.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2, shuffle=False)


# In[4]:


#ii).Using scikit learn perform a LDA on the dataset. Find out the number of components in the projected subspace.

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()
clf.fit(X_train, y_train)


# In[5]:


Y_predict = clf.predict(X_test)


# In[16]:


import pandas as pd 
predict_ =list(zip(y_test, Y_predict))  

df = pd.DataFrame(predict_, columns = ['Actual Value', 'Predicted Value']) 


# In[17]:


df.head()


# In[18]:


clf.transform(X_test)


# In[49]:


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, Y_predict)
#print(cm)
print('Accuracy of the LDA model :' + str(accuracy_score(y_test, y_predict)*100))


# In[27]:


# ransform the dataset and fit a logistic regression and observe the accuracy.

# Compare it with the previous model based on PCA in terms of accuracy and model complexity.

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0).fit(X_train, y_train)


# In[43]:


y_predict = clf.predict(X_test)
import pandas as pd 
predict_ =list(zip(y_test, y_predict))  

df = pd.DataFrame(predict_, columns = ['Actual Value', 'Predicted Value'])
df.head()


# In[51]:


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_predict)
# print(cm)
print('Accuracy of the  logistic regression model ' + str(accuracy_score(y_test, y_predict)*100))


# In[ ]:




