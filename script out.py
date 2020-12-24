# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:08:13 2020

@author: DELL
"""

def g(x):
    return x*x+3
def b(f,A):
    I = set()
    for a in A:
        print("f(",a,")=",f(a))
        I.add(f(a))
    return I

print (b(g,{-1,0,1,2}))
