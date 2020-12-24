#!/usr/bin/env python
# coding: utf-8

# In[131]:


def checkOrder(inpu, pattern):  
    occurence_array = [-1]* len(inpu)
    flag = 0
    count_ne = 0
    ptrlen = len (pattern)
    for i in range(0,len(pattern)):
        for j in range(0,len(inpu)):
            if(inpu[j].find(pattern[i]) != -1):
                occurence_array[j] = j
    for i in range(0,len(occurence_array)):
        if(occurence_array[i] == -1):
            count_ne = count_ne +1
    for i in range(0,count_ne):
        occurence_array.remove(-1)
    while i < len(occurence_array): 
        if(occurence_array[i] < occurence_array[i - 1]): 
            flag = 1
        i += 1
    if( flag == 0 and len(occurence_array) != 0):
        return True
    else:
        return False


# In[132]:


pattern = ["h","i"]
str = "hi how are you"
checkOrder(str,pattern)


# In[74]:


str[0].find(pattern[0])


# In[66]:


pattern[0]


# In[ ]:




