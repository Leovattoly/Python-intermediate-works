# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:26:07 2020

@author: DELL
"""

def cipher_fun(c,d):
    if c in d:
        return (d[c])

alpha_lst = list()
caesar_lst = list()
alpha_lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
caesar_lst = list("DEFGHIJKLMNOPQRSTUVWXYZABC")

d = dict(zip(alpha_lst,caesar_lst))
encry_lst = list()
f = open("demofile.txt", "r")
content = f.read()
for c in content:
    encry_lst += [cipher_fun(c,d)]
print(encry_lst)
    
    