#!/usr/bin/env python
# coding: utf-8

# In[3]:


# How to do program that prompts the user for a string and then displays a count of each of the vowels (a, e, i, o, u) 
# and the total number of vowels contained in that string.

def vowels_chk(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 
      
# Driver Code 
string = input("Enter the string: ")
vowels = "AaEeIiOoUu"
vowels_chk(string, vowels); 


# In[24]:


# How to do a program that accepts a string in the format Age.FirstName and returns the value FirstName is Age years old. 

def counting_name(string):
    for i in range (len(string)):
        if (string[i] == "."):
            return i
        
    

string = input("Enter the input (Age.FirstName format): ")
dot = counting_name(string)
name = string[dot+1:]
age = int(string[0]+string[1])
print(name," is ",age,"years old. Length of ",name," is ",len(name))


# In[ ]:




