# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 08:37:15 2022

@author: 13687
"""

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

m = loadmat("C:/Users/13687/Documents/化学计量学课件/ginseng.mat")
t = m['t'][:,0]
X = m['X']

for i in range(X.shape[1]):
    x = X[:,i] + i*100
    plt.plot(t, x)
    
plt.xlabel('retention time(min)')
plt.ylabel('instensity(mAU)')
plt.legend(loc='upper left')

plt.show()

u, s, vh = np.linalg.svd(X.T, full_matrices=False)
s1 = np.diag(s)
T = np.dot(u,s1)

N = T.shape[0]
colors = np.random.rand(N)

for i in range(32):
    plt.text(T[0,i], T[1,i], i+1)
    
plt.scatter(T[0,:], T[1,:], s = 32, c = colors, alpha = 0.5)


        



    





