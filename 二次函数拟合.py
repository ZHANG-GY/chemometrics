# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:07:26 2022

@author: 13687
"""

# def calc_mean_std(x, mean_std) :
#     y = 0
#     if mean_std == 1 :
#         for i in x :
#             y += i
#         return y/len(x)
#     elif mean_std == 0 :
#         for i in x :
#             y += i
#         y1 = 0
#         for i in x :
#             y1 += (i - y/len(x))**2
#         std = (y1/(len(x)-1))**0.5
#         return std
#     else:
#         print('wrong ,mean_std =0/1')
        
import numpy as np

y = np.array([0.05, 0.10, 0.15, 0.20, 0.25]) 
x = np.array([1.00, 4.05, 9.10, 15.09, 24.52]) 
x1 = x**2
X = np.row_stack((x1,x))
X = np.row_stack((X,[1,1,1,1,1]))

m1 = np.dot(X,X.T)
m2 = np.linalg.inv(m1)
m3 = np.dot(m2,X)
b = np.dot(m3,y)

x = 10.50
Y = np.dot(np.array([x**2,x,1]),b)        