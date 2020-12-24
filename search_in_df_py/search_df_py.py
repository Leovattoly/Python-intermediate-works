#!/usr/bin/env python
# coding: utf-8

# In[48]:


def search_desc(var1,df):
    k =  df[df.eq(var1).any(1)]
    return k


# In[49]:


# Import modules
import pandas as pd

# creating a data frame from lists
raw_data = {'Description': ['Moby Dick', 'War and Peace', 'Desk'], 
        'Category': ['Book', 'Book', 'Antique'], 
        'Value': [10.0, 50.0, 250.0], 
        'Amount': [1,1,1]}
# list onverting to data frame
df = pd.DataFrame(raw_data, columns = ['Description', 'Category', 'Value', 'Amount'])

# Asking for the user input 
var1 = input("Enter item's description:" )
item = search_desc(var1,df)
if item.empty== False:
    print(item)
    
else:
    print("Description does not exist.")


# In[ ]:





# In[8]:





# In[ ]:




