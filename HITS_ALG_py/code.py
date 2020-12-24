#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing modules 
import networkx as nx 
import matplotlib.pyplot as plt 

G = nx.Graph() 

G.add_edges_from([('wikipedia','Bing'),('wikipedia','Google'),('Google','wikipedia'),('Google','Yahoo'),('Google','Rediff'),('Google','Astalavista'),('Google','Bing'),('Yahoo','Astalavista'),('Yahoo','Bing'),('Astalavista','Google'),('Astalavista','Bing'),('Rediff','Bing'),('Bing','Google')]) 

plt.figure(figsize =(20, 20)) 
nx.draw_networkx(G, with_labels = True) 

hubs, authorities = nx.hits(G, max_iter = 50, tol =0.04,normalized = True) 
# The in-built hits function returns two dictionaries keyed by nodes 
# containing hub scores and authority scores respectively. 

print("Hub Scores: ", hubs) 
print("Authority Scores: ", authorities) 


# In[ ]:




