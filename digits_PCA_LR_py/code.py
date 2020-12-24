#!/usr/bin/env python
# coding: utf-8

# In[64]:


# importing digit dataset
from sklearn.datasets import load_digits
digits = load_digits()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)

data = digits.images.reshape((n_samples, -1))


# In[38]:


# i)Load digits dataset from scikit learn and write a helper function to plot the image using matplotlib.

import matplotlib.pyplot as plt

n = int(input("Enter the Digit no to be plotted: "))

#Display the first digit
plt.figure(1, figsize=(5, 4))
plt.imshow(digits.images[n], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()


# In[67]:


# Make a train -test split with 20% of the data set aside for testing. 
# Fit a logistic regression model and observe the accuracy.

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2, shuffle=False)

clf = LogisticRegression(random_state=0).fit(X_train, y_train)

# predicting using the model
y_predict = clf.predict(X_test)
 
from sklearn.metrics import accuracy_score
print('Accuracy of the  logistic regression model ' + str(accuracy_score(y_test, y_predict)*100))


# In[73]:


# iii).Using scikit learn perform a PCA transformation such that the transformed dataset can explain 95% of the variance 
# in the original dataset. 
# Find out the number of components in the projected subspace.

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.decomposition import PCA

pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

#print(explained_variance)

# It can be seen that first principal component is responsible for 1.5% variance. Similarly, 
# the second principal component causes 1.5 % variance in the dataset. 
# Collectively we can say that (1.5 * 64) 96 % percent of the classification information contained 
# in the feature set is captured by the first two principal components.
# Taht is the reason for choosing 64 as n_component in following PCA

# iv).Transform the dataset and fit a logistic regression and observe the accuracy. 

from sklearn.decomposition import PCA

pca = PCA(n_components=64)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

clf = LogisticRegression(random_state=0).fit(X_train, y_train)

# predicting using the model
y_predict = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print('Accuracy of the  logistic regression model after PCA' + str(accuracy_score(y_test, y_predict)*100))


# In[80]:



# v).Compute the confusion matrix and count the number of instances that has gone wrong. 
# For each of the wrong sample, plot the digit along with predicted and original label.

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)
print(cm)
count = 0
for i in range(10):
    for j in range (10):
        if i != j:
            count = count +1
print ("Number of instances that has gone wrong: ",count)

from matplotlib import pyplot as plt
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(10):
    for j in range (10):
        if i != j:
            ax = fig.add_subplot(9, 10, i + 1, xticks=[], yticks=[])
            ax.imshow(digits.images[j], cmap=plt.cm.binary, interpolation='nearest')
            # label the image with the target value
            ax.text(0, 7, str(digits.target[i]))


# In[ ]:




