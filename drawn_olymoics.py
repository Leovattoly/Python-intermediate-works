# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:20:50 2020

@author: DELL
"""

#Python Program to draw Olympics logo in Turtle Programming
'''import turtle
 
t = turtle.Turtle()
t.pensize(6) #Set the thickness of the pen to 6
firstRowColors = ["blue", "black", "red"] #firstRowColors is a list of colors that are present in the first row of logo
for i in range(3):
  t.penup()
  t.pencolor(firstRowColors[i])
  t.goto(i*110, 0)
  t.pendown()
  t.circle(50)
 
secondRowColors = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  t.penup()
  t.pencolor(secondRowColors[i])
  t.goto(i*55, -50)
  t.pendown()
  t.circle(50)'''
  import turtle
  t = turtle.Turtle()
  t.pensize(6)
  t.pencolor("red")
  for i in range(3):
      t.right()
      t.stamp()
      t.forward(1+i)
  t.pendown()
  t.circle(50)
      