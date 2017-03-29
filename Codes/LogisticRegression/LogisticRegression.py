import numpy as np
import matplotlib.pyplot as plt

# Data Initialization
width = np.array([ 30, 34, 203, 40, 199, 36, 150, 33, 190, 166, 90 ])
height = np.array([ 166, 183, 23, 192, 30, 177, 19, 154, 40, 30, 10 ])
t_set = np.array([
    width,
    height
])
y = np.array([ 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0])
n = t_set.shape[0]

# 가중치 설정
# 가중치를 너무 높게 설정하면 경사하강이 잘 안되었다.
theta = np.random.rand(n) * 0.05
print(theta)

# Sigmoid 함수이자 가설함수 H(x)
def sigmoid(X):
    return 1.0 / (1.0 + np.exp(- X))

lr = 0.001
learning_time = 200000

for i in range(learning_time):
    dj = np.dot(sigmoid(np.dot(t_set.T, theta)) - y, t_set.T) / n
    theta = theta - lr * dj

_x = np.linspace(0, 250, 251)
t1, t2 = theta[0], theta[1]
_y = -(t1 * _x) / t2

plt.scatter(width, height, marker='o')
plt.plot(_x, _y)
plt.show()
