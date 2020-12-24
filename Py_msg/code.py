# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:55:21 2020

@author: Leo
"""

list_line = []
date= []*50
mini = []
address = []
msg = []
splitted = []

f = open("messages", "r")
for chunk in iter(lambda: f.readline(), ''):
    list_line.append(f.readline())
    
print(len(list_line))
print(list_line[2])
''' i=0
for i in range(len(list_line)):
    splitted.append( list_line[i].split(":"))

for i in range(49):
    msg.append(splitted[i][3])

for i in range(49):
    address.append(splitted[i][2])

# using naive method 
# to convert lists to dictionary 
res = {} 
for key in address: 
    for value in msg: 
        res[key] = value 
        msg.remove(value) 
        break 
print ("Resultant dictionary is : " +  str(res))
'''
