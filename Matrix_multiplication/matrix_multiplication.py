#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[8]:



def matrix_mul(A,B):
    result = [[0,0, 0],
              [0, 0, 0],
              [0, 0,0]]

    for i in range(len(A)):
       # iterate through columns of B
       for j in range(len(B[0])):
           # iterate through rows of B
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1,3, 4],
     [2, 5, 7],
     [5, 9,6]]
B = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]] 
        #A*B = [[1 3 4] [2 5 7] [5 9 6]]
print(matrix_mul(A,B))


# In[ ]:




