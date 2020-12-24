#!/usr/bin/env python
# coding: utf-8

# In[21]:



i = 0
numStarsString = "10"
numStars [0] *100
while (float(numStarsString) >0):
    numStarsString = input("Enter rating for featured movie: ")
    numStars [i]= float(numStarsString)
    i= i+1

print(numStars)
    
    
    
    


# In[40]:



i = 0
numStarsString = "10"  # random value for working the while loop
numStars =  [0] *100   # initializing a list with 100 space

# iteration for accepting the input  
while (float(numStarsString) >= 0):
    numStarsString = input("Enter rating for featured movie: ")
    numStars [i]= float(numStarsString)
    i= i+1
    
# deleting the unwanted datas including the -ve value
del numStars[i-1:100]   

# finding the total and average of the list item

total = 0
for ele in range(0, len(numStars)): 
    total = total + numStars[ele] 

averageStars = total / (i-1)
print("Average Star Value: " + str(averageStars))
    
    


# In[26]:


0
0


# In[ ]:




