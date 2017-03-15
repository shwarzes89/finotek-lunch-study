import numpy as np
import pandas as pd

def compute_cost(x, y, w):
    return np.sum(np.power(((x* w.T)- y), 2)) / len(x)

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

        print(parameters)
        for j in range(parameters):
            print(x)
            term = np.multiply(error, x[:,j])
            temp[0,j] = w[0,j] - ((learning_rate / len(x)) * np.sum(term))

        w = temp
        cost[i] = compute_cost(x, y, w)

    return w, cost


def get_test_set():
    return pd.read_csv("data.txt", header=None, names=["q1", "q2", "mid", "final"])

def main():

    data = get_test_set()

    print("\n", data.head(), "\n")

    # set X (training data) and y (target variable)
    cols = data.shape[1]
    x = data.iloc[:,0:cols-1]
    y = data.iloc[:,cols-1:cols]

    # convert to matrices and initialize theta
    x = np.matrix(x.values)
    y = np.matrix(y.values)
    w = np.matrix(np.array([0,0,0]))

    # perform linear regression on the data set
    g, cost = gradient_descent(x, y, w, 0.0000001, 500)
    print("\n", "weight matrix", g)


if __name__ == "__main__":
    main()

