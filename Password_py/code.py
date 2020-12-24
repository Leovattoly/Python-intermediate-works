#!/usr/bin/env python
# coding: utf-8

# In[3]:


# getpass.getpass() to read password 
import getpass 
  
print("Enter Password: ")

try: 
    p = getpass.getpass() 
except Exception as error: 
    print('ERROR', error) 
else: 
    f = open("password.txt", "r")
    if f.readline() == p:
        print("Password is correct")
    else: 
        print("Wrong Password")


# In[ ]:





# In[ ]:




