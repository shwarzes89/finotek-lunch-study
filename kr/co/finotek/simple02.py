import numpy as np
x = np.array([0,1]) # 입력
w = np.array([0.5,0.5])#가중치
b = -0.7
w*x

print(np.sum(w*x))

np.sum(w*x) + b
