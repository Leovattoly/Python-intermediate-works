# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:32:37 2020

@author: DELL
"""
# 1. Write Python code to see the last five instances. 

instances = [1,2,3,4,5,6,7,8,9,10]
print("LastFive values of the given list:\n")
print(instances[-5:])

# 2. Write Python code to sort the data frame based on sepalLength and sepalWidth in Descending order .

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris_df.head(5))
iris_df.sort_values(by=['sepal length (cm)','sepal width (cm)'], ascending=True)
print("After Sorting\n")
print(iris_df)

#5. Write Python code to download the Federal Reserve economic data (FRED/GDP) in Quandl data delivery platform and display first 5 records

import quandl
df = quandl.get("FRED/GDP", rows=5,returns="numpy")
print("Last Five rows of Data\n")

print(df.head(5))

