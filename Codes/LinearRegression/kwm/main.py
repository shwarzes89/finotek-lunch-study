import numpy as np
import pandas as pd

def compute_cost(x, y, w):
    return np.sum(np.power(((x* w.T)- y), 2)) / (2 * len(x))

def test_compute_cost():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 3, 4, 2, 1])
    return compute_cost(x, y, 0.1)

def gradient_descent(x, y, w, learning_rate, iters):
    temp = np.matrix(np.zeros(w.shape))
    parameters = int(w.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (x * w.T) - y

        for j in range(parameters):
            term = np.multiply(error, x[:,j])
            temp[0,j] = w[0,j] - ((learning_rate / len(x)) * np.sum(term))

        w = temp
        cost[i] = compute_cost(x, y, w)
        print(w)

    return w, cost


def get_test_set():
    return pd.read_csv("data.txt", header=None, names=["q1", "q2", "mid"])

def main():

    data = get_test_set()

    # add ones column
    data.insert(0, 'Ones', 1)

    # set X (training data) and y (target variable)
    cols = data.shape[1]
    X2 = data.iloc[:,0:cols-1]
    y2 = data.iloc[:,cols-1:cols]

    # convert to matrices and initialize theta
    X2 = np.matrix(X2.values)
    y2 = np.matrix(y2.values)
    theta2 = np.matrix(np.array([0,0,0]))

    # perform linear regression on the data set
    g2, cost2 = gradient_descent(X2, y2, theta2, 0.0001, 500)

    print(g2)

if __name__ == "__main__":
    main()

