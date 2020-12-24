#!/usr/bin/env python
# coding: utf-8

# In[2]:


# i).Load the file "zoo.data" and look at the info and first five rows. The first column

# denotes the animal name and the last one specifies a high-level class for the

# corresponding animal.




# inserting data 
import pandas as pd
df = pd.read_csv("zoo.csv")
df.head()


# In[4]:


# ii). Find out the unique number of high level class. storing unique value in a variable

unique_value = df["class_type"].nunique() 
print("unique number of high level class:",unique_value)


# In[29]:


# iii). Use the 16-intermediate feature and perform an agglomerative clustering.

from sklearn.cluster import AgglomerativeClustering
x =df.iloc[:,1:17].values # Features 
y_true = df.iloc[:,17].values
clustering = AgglomerativeClustering(n_clusters= 7).fit(x)

# predicted clustering labels
y_predicted = clustering.labels_


# In[31]:


#Compute the mean squared error by comparing the actual class and predicted high level class.

from sklearn.metrics import mean_squared_error

print("Mean square error: ",mean_squared_error(y_true, y_predicted))


# In[ ]:




