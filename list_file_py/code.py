# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:16:42 2020

@author: DELL
"""

# creating the list 

list_1 = ["sldlsd",
          'dsdsd',
          'dsdsd',
          'dsdgf']
list(list_1)

# opening a file to write
text_file = open("sample.txt", "w")

# writing each item in the row with a new line 
for i in range(len(list_1)):
    b = text_file.write(format(list_1[i]))
    text_file.write("\n")	
text_file.close()