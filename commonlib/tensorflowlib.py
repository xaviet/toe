#! /usr/bin/python3
# coding=utf-8
'''
  tensorflowlib.py
'''

import tensorflow as tf


def test():
  my_graph = tf.Graph()
  with tf.Session(graph=my_graph) as sess:
    x = tf.constant([1, 3, 6])
    y = tf.constant([1, 1, 1])
    op = tf.add(x, y)
    result = sess.run(fetches=op)
    print(result)
  print(op)


if (__name__ == '__main__'):
  test()

#from tensorflow.examples.tutorials.mnist import input_data
#import tensorflow as tf
#import time
#import commonlib
#import matplotlib.pyplot as plt

#def getMnist():
#dataSetPath = 'd:\\temp\\data\\'
#mnist = input_data.read_data_sets(dataSetPath, one_hot=True)
#return (mnist)

#@commonlib.spentTime
#def ex0(trainTime=256):
#mnist = getMnist()
#x = tf.placeholder('float', [None, 784])
#W = tf.Variable(tf.zeros([784, 10]))
#b = tf.Variable(tf.zeros([10]))
#y = tf.nn.softmax(tf.matmul(x, W) + b)
#y_ = tf.placeholder('float', [None, 10])
#cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
#train_step = tf.train.GradientDescentOptimizer(0.01).minimize(
#cross_entropy)
#init = tf.initialize_all_variables()
#sess = tf.Session()
#sess.run(init)
#for i in range(trainTime):
#batch_xs, batch_ys = mnist.train.next_batch(100)
#sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
#rt = sess.run(
#accuracy, feed_dict={x: mnist.test.images,
#y_: mnist.test.labels})
#print(rt)
#return (rt)

#@commonlib.spentTime
#def ex1(trainTime=256):
#mnist = getMnist()
#sess = tf.InteractiveSession()
#x = tf.placeholder('float', shape=[None, 784])
#y_ = tf.placeholder('float', shape=[None, 10])
#W = tf.Variable(tf.zeros([784, 10]))
#b = tf.Variable(tf.zeros([10]))
#sess.run(tf.initialize_all_variables())
#y = tf.nn.softmax(tf.matmul(x, W) + b)
#cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
#train_step = tf.train.GradientDescentOptimizer(0.01).minimize(
#cross_entropy)
#for i in range(trainTime):
#batch = mnist.train.next_batch(50)
#train_step.run(feed_dict={x: batch[0], y_: batch[1]})
#correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
#rt = sess.run(
#accuracy, feed_dict={x: mnist.test.images,
#y_: mnist.test.labels})
#print(rt)
#return (rt)

#@commonlib.spentTime
#def ex2(trainTime=256):
#def weight_variable(shape):
#initial = tf.truncated_normal(shape, stddev=0.1)
#return (tf.Variable(initial))

#def bias_variable(shape):
#initial = tf.constant(0.1, shape=shape)
#return (tf.Variable(initial))

#def conv2d(x, W):
#return (tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME'))

#def max_pool_2x2(x):
#return (tf.nn.max_pool(
#x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'))

#mnist = getMnist()
#x = tf.placeholder('float', shape=[None, 784])
#y_ = tf.placeholder('float', shape=[None, 10])
#sess = tf.InteractiveSession()
#W_conv1 = weight_variable([5, 5, 1, 32])
#b_conv1 = bias_variable([32])
#x_image = tf.reshape(x, [-1, 28, 28, 1])
#h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
#h_pool1 = max_pool_2x2(h_conv1)
#W_conv2 = weight_variable([5, 5, 32, 64])
#b_conv2 = bias_variable([64])
#h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
#h_pool2 = max_pool_2x2(h_conv2)
#W_fc1 = weight_variable([7 * 7 * 64, 1024])
#b_fc1 = bias_variable([1024])
#h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
#h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
#keep_prob = tf.placeholder('float')
#h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#W_fc2 = weight_variable([1024, 10])
#b_fc2 = bias_variable([10])
#y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
#cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
#train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
#correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
#sess.run(tf.initialize_all_variables())
#for i in range(trainTime):
#batch = mnist.train.next_batch(50)
#if (i % 100 == 0):
#train_accuracy = accuracy.eval(
#feed_dict={x: batch[0],
#y_: batch[1],
#keep_prob: 1.0})
##print(time.strftime('%H:%M:%S'))
##print('step␣%d,␣training␣accuracy␣%g'%(i, train_accuracy))
#train_step.run(
#feed_dict={x: batch[0],
#y_: batch[1],
#keep_prob: 0.5})
#rt = accuracy.eval(feed_dict={
#x: mnist.test.images,
#y_: mnist.test.labels,
#keep_prob: 1.0
#})
#print(rt)
#return (rt)

#from tensorflow.examples.tutorials.mnist import fully_connected_feed

#@commonlib.spentTime
#def ex3(trainTime=256):
#rt = 0
#print(rt)
#return (rt)

#def test():
#trainTime = [16, 64, 256, 1024]
#r0 = []
#r1 = []
#r2 = []
#r3 = []
#for el0 in trainTime:
#r0.append(ex0(el0))
#r1.append(ex1(el0))
#r2.append(ex2(el0))
#r3.append(ex3(el0))
#print(trainTime)
#print(r0)
#print(r1)
#print(r2)
#print(r3)
#plt.plot(trainTime, r0, label='ex0')
#plt.plot(trainTime, r1, label='ex1')
#plt.plot(trainTime, r2, label='ex2')
#plt.plot(trainTime, r3, label='ex3')
#plt.show()

#if (__name__ == '__main__'):
#test()
