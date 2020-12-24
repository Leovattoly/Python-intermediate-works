#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np  

def powers_in_range(n,mn,mx):
    count = 0
    for i in range(mn,mx+1):
        root = kthroot(i,n)
        if(int(root) == root):
            count = count +1
    return count

def kthroot(n,k):
    return pow(k, ((1.0 / k) * (np.log(n) / np.log(k)))) 

powers_in_range(2,49,65)
            


# In[ ]:




