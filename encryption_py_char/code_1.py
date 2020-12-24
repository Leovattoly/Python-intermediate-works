# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:34:16 2020

@author: DELL
"""


def cipher_fun(c,d):
    if c in d:
        return (d[c])

alpha_lst = list()
numeric_lst = list()
alpha_lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(1,27):
    numeric_lst += [i]

d = dict(zip(alpha_lst,numeric_lst))
encry_lst = list()
f = open("demofile.txt", "r")
content = f.read()
for c in content:
    encry_lst += [cipher_fun(c,d)]
print(encry_lst)
    
    