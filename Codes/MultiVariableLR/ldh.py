
# coding: utf-8

# In[130]:

import numpy as np


# In[131]:

num = 3


# In[132]:

X = np.array( [
    [73, 93, 89, 96, 73],
    [80, 88, 91, 98, 66],
    [75, 93, 90, 100, 70]
] )
n = X.shape[1]
_x = np.vstack([np.ones(n), X]).T
_y = np.array([152, 185, 180, 196, 142])

print(_x)
m, n = np.shape(_x)


# In[191]:

_weights = np.random.rand(n)

print("초기 theta:")
print(_weights)

h = np.dot(_x, _weights)
cost = h - _y
gradient = np.dot(_x.T, cost) / m

print(_x.T)

print("경사 = ")
print(gradient)


# In[182]:

# do gradient descent
numIterations = 100000
lr = 0.00001

for i in range(0, numIterations):
    h = np.dot(_x, _weights)
    cost = h - _y
    gradient = np.dot(_x.T, cost) / m
    
    _weights = _weights - lr * gradient

print("결과 theta: =", _weights)
print(np.dot(_weights, _x[0]))


# In[ ]:



