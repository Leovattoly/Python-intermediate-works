# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:48:40 2020

@author: DELL
"""

import turtle
style = ('Courier', 10, 'italic')
t = turtle.Turtle()
t.shape("arrow")
t.shapesize(10)
t.stamp()
t.forward(120)
t.write('Hello!', font=style)
t.hideturtle()
t.pendown()