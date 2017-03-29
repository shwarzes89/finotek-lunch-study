import tensorflow as tf
import numpy as np


xy = np.loadtxt('train_set.txt', unpack=True, dtype='float32')

x_data = np.transpose(xy[:2])
y_data = np.transpose(xy[2:])

X = tf.placeholder("float", [None, 2])
Y = tf.placeholder("float", [None, 3])

W = tf.Variable(tf.zeros([2, 3]))

# softmax 알고리듬 적용. X*W = (15x2) * (2x3) = (15x3)
hypothesis = tf.nn.softmax(tf.matmul(X, W))

# cross-entropy cost 함수
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), reduction_indices=1))

learning_rate = 0.00001
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for step in range(40000):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            feed = {X: x_data, Y: y_data}
            print('{:4} {:8.6}'.format(step, sess.run(cost, feed_dict=feed)), *sess.run(W))
