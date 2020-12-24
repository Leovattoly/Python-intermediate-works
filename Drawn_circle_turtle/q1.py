# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:27:36 2020

@author: DELL
"""

import turtle
t = turtle.Turtle()
t.pensize(1)
t.pencolor("red")
for i in range (100) :
    t.right(40)
    t.stamp()
    t.forward(i+1)
t.pendown()
t.circle()

