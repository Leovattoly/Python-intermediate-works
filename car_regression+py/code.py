# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:04:18 2020

@author: DELL
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('data.csv')
# print(df)
x = np.array(df["Age"]).reshape((-1, 1))
y = np.array(df["Mileage"])
model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
# Intercept
b =  float(model.intercept_)
# slope
a = float(model.coef_)
print("Regression Equation: \n")
print("y = ",a,"x+ ",b)

# plotting data with regression line

plt.plot(x, y, 'o')

plt.plot(x, a*x + b)

# predicting the mileafe of a car having 8 year old

y_pred = model.predict(np.array(8).reshape((-1, 1)))

print("Mileage of a car having 8 year old (Predicted by model): ",float(y_pred))