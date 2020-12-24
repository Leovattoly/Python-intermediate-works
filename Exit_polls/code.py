# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:55:29 2020

@author: DELL
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.model_selection import cross_val_score # Cross validation for training data
from sklearn.linear_model import LogisticRegression # Classification
from sklearn.metrics import confusion_matrix # Confusion matrix for test data

# inserting data 
df = pd.read_csv("data.txt")
# print(df)

print(df.shape)
df.head()

#check for null values
df.isnull().sum()

# Bivariate line chart
df.plot.line()

# splitting data into train and test 
X = df[] # value to be predicteed
y = df[] # features in dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 1. Apply Logistic Regression and LDA (linear discriminant analysis). 

lda = LinearDiscriminantAnalysis()
x_train = lda.fit_transform(x_train, y_train)
x_test = lda.transform(x_test)

# Linear kernel SVM
classifier = LogisticRegression(random_state = 42)
classifier.fit(x_train, y_train)

# Applying k-Fold Cross Validation
print("Applying k fold cross validation ")
accuracies = cross_val_score(estimator=classifier,
                             X=x_train, y=y_train,
                             cv = 10, n_jobs=-1)
print("Cross validation accuracies :")
print(accuracies)
print("Cross validation mean :",accuracies.mean())
print("Cross validation std :",accuracies.std())


# evaluate bagging algorithm for classification
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import BaggingClassifier
# define the model
model = BaggingClassifier()
# evaluate the model
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
# report performance
print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
