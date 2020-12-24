#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sklearn.datasets as datasets
import sklearn.model_selection as ms
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler


digits = datasets.load_digits();

# Perform Standardization of digits.data and store the transformed data in variable digits_standardized.
X = digits.data
scaler = StandardScaler()
scaler.fit(X)
digits_standardized = scaler.transform(X)

y = digits.target

X_train, X_test, y_train, y_test = train_test_split(digits_standardized, y, random_state=30, stratify=y)

#print(X_train.shape)
#print(X_test.shape)

# Build another SVM classifier from X_train set and Y_train labels, with default parameters. Name the model as svm_clf2.
from sklearn.svm import SVC
svm_clf2 = SVC().fit(X_train, y_train)
print("Accuracy ",svm_clf2.score(X_test,y_test))


# In[5]:


import sklearn.datasets as datasets
import sklearn.model_selection as ms
from sklearn.model_selection import train_test_split


digits = datasets.load_digits();
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=30, stratify=y)

#print(X_train.shape)
#print(X_test.shape)

from sklearn.svm import SVC
svm_clf = SVC().fit(X_train, y_train)
print("Accuracy",svm_clf.score(X_test,y_test))


# In[ ]:




