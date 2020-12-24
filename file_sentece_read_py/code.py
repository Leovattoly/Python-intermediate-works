#!/usr/bin/env python
# coding: utf-8

# In[1]:


L = ["1 Canon 5D Mark IV $4567.99 2500 \n", "3 Nikon battery NB45 $65.99 140 \n"] 
  
# writing to file 
file1 = open('camera.txt', 'w') 
file1.writelines(L) 
file1.close() 
  
# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip())) 


# In[28]:


# Using readlines() 

file_name = input("Enter the file name: ")
file_name = file_name +'.txt'
file1 = open(file_name, 'r') 
Lines = file1.readlines() 
  
total_price = 0
total_weight = 0
count = 0
# Strips the newline character 
for line in Lines: 
    line_content = line.strip()
    start = line_content.find('$') 
    end = line_content.rfind(' ',0,len(line_content))
    price = float((line_content[start+1:end]))
    total_price = total_price+price
    weight = float (line_content[end+1:-1])
    total_weight = total_weight +weight
postage = (total_weight/1000 ) *10.50
total_amount_order = postage + total_price
print("\nItems total price = $",total_price)
print("\nTotal weight = {:.1f}".format(total_weight),"kg")
print("\nPostage  = $",postage)
print("\nOrder total price = $",total_amount_order)




# In[ ]:





# In[ ]:




