#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1)Read the data file and check for any missing values

# inserting data 
import pandas as pd
df = pd.read_csv("Project_Data.csv")
df.headad()


# In[3]:


# checking for any NA values or missing values

import seaborn as sns

sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis")


# In[31]:


# renaming the column

df = df.rename(columns = {"Sales of Wheat in tons":"country "}) 


# In[42]:


# making a copy of dataframe

df_copy = df[["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007"]]
df_copy.head()


# In[46]:


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from yellowbrick.cluster import KElbowVisualizer

# Instantiate the clustering model and visualizer
model = KMeans()
visualizer = KElbowVisualizer(model, k=(4,12))
visualizer.fit(df)        # Fit the data to the visualizer
visualizer.show()        # Finalize and render the figure


# In[47]:


#As we need to make this across years we need to apply PCA first.

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(df_copy)


# In[ ]:


# Then try to apply K means

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)

print(kmeans.labels)
print(kmeans.cluster_centers_)


# In[51]:


# Then try to apply Hierarchical clustering 

from sklearn.cluster import AgglomerativeClustering
h_clustering = AgglomerativeClustering(n_clusters=2)
h_clustering.fit(df_copy)


# In[ ]:




