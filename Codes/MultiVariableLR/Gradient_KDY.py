# Lab 4 Multi-variable linear regression
import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

x_data = [[73., 80., 75.], [93., 88., 93.],
          [89., 91., 90.], [96., 98., 100.], [73., 66., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142.]]


# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
alpha = 1e-5

hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize using TF
optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(cost)

# Not using TF
gradient = tf.reduce_mean((hypothesis - y_data) * x_data)
descent = W - alpha * gradient
descent_b = b - alpha * gradient
update = W.assign(descent)
update_b = b.assign(descent_b)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(200):
    cost_val, hy_val, _, _ = sess.run(
        [cost, hypothesis, update, update_b], feed_dict={X: x_data, Y: y_data})
    #if step % 10 == 0:
    print(step, cost_val)
    print(sess.run(W))
    print(sess.run(b))
    print(hy_val)
    print("===========")

'''
0 Cost:  7105.46
Prediction:
 [[ 80.82241058]
 [ 92.26364136]
 [ 93.70250702]
 [ 98.09217834]
 [ 72.51759338]]
10 Cost:  5.89726
Prediction:
 [[ 155.35159302]
 [ 181.85691833]
 [ 181.97254944]
 [ 194.21760559]
 [ 140.85707092]]

...

1990 Cost:  3.18588
Prediction:
 [[ 154.36352539]
 [ 182.94833374]
 [ 181.85189819]
 [ 194.35585022]
 [ 142.03240967]]
2000 Cost:  3.1781
Prediction:
 [[ 154.35881042]
 [ 182.95147705]
 [ 181.85035706]
 [ 194.35533142]
 [ 142.036026  ]]

'''