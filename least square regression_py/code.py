#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Providing data
x = np.array([5, 10,15,20, 25,30,35,40, 45, 50]).reshape((-1, 1))
y = np.array([17,24,31,33,37,37,40,40,42,41])

# Least squares regression 
model = LinearRegression()

# model feeding with data
model.fit(x, y)

# y intercept 
c = model.intercept_

# Slope (m)

m =model.coef_

# y = mx + c

y_ = m*x + c
plt.scatter(x, y, color='r')
plt.plot(x, y_, '-b')
plt.title('Graph of y=mx+c')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()


# In[9]:


# Power equation 

# Take the natural log of both sides:

print("Power Equation : y = ",float(m),"x +",c)


# In[20]:


# Saturation - growth rate equation

# Providing data
x = np.array([5, 10,15,20, 25,30,35,40, 45, 50])
y = np.array([17,24,31,33,37,37,40,40,42,41])

eq = np.polyfit(np.log(x), y, 1)
print("Saturation - growth rate equation y = ",float(eq[0]),"x +",eq[1])


# In[21]:


# d ) Parabola plot 

y_ = m*x + c
plt.plot(x,y)
plt.scatter(x, y, color='r')
plt.plot(x, y_, '-b')
plt.title('Graph of y=mx+c')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()


# In[ ]:




