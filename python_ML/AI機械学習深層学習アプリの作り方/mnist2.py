from sklearn import datasets, model_selection
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np

mnist = datasets.fetch_mldata('MNIST original', data_home='./mnist')
x = mnist.data / 255
y = OneHotEncoder().fit_transform(mnist.target.reshape(-1,1)).A
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

IMG_SIZE = 28
IMG_LEN = IMG_SIZE * IMG_SIZE
FILTER_SIZE = 3
FILTER_NUM = 16
ALL_CON = 512
CLASS_NUM = 10

x = tf.placeholder(tf.float32, shape=[None, IMG_LEN], name='input')
y_ = tf.placeholder(tf.float32, shape=[None, CLASS_NUM], name='output')

x_image = tf.reshape(x, [-1, IMG_SIZE, IMG_SIZE, 1])

with tf.name_scope("conv1"):
    w_conv1 = tf.Variable(tf.truncated_normal([FILTER_SIZE, FILTER_SIZE, 1, FILTER_NUM], stddev=0.1), name='w_conv1')
    b_conv1 = tf.Variable(tf.truncated_normal([FILTER_NUM], stddev=0.1), name='b_conv1')

conv1 = tf.nn.conv2d(x_image, w_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1
pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

with tf.name_scope("dense"):
    w_dense = tf.Variable(tf.truncated_normal([14 * 14 * FILTER_NUM, ALL_CON], stddev=0.1), name='w_dense')
    b_dense = tf.Variable(tf.truncated_normal([ALL_CON], stddev=0.1), name='b_dense')

pool1_flat = tf.reshape(pool1, [-1, 14 * 14 * FILTER_NUM])

dense = tf.nn.relu(tf.matmul(pool1_flat, w_dense) + b_dense, name='dense')

keep_prob = tf.placeholder(tf.float32)

drop = tf.nn.dropout(dense, keep_prob)

with tf.name_scope("all"):
    w_all = tf.Variable(tf.truncated_normal([ALL_CON, CLASS_NUM], stddev=0.1), name='w_all')
    b_all = tf.Variable(tf.truncated_normal([CLASS_NUM], stddev=0.1), name='b_all')

y_conv = tf.nn.softmax(tf.matmul(drop, w_all) + b_all)

cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch = 100
epoch = 100
total = int(x_train.shape[0]/batch)

with tf.name_scope('summary'):
    tf.summary.scalar('cross_entropy', cross_entropy)
    tf.summary.scalar('accuracy', accuracy)
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter('./logs', sess.graph)

for e in range(epoch):
    for i in range(total):
        x_batch = x_train[i*batch:(i+1)*batch]
        y_batch = y_train[i*batch:(i+1)*batch]
        train_accuracy = sess.run(train_step, feed_dict={x:x_batch,y_: y_batch, keep_prob: 0.5})
        #train_entropy = sess.run(cross_entropy, feed_dict={x:x_batch,y_: y_batch, keep_prob: 0.5})
        train = sess.run(merged, feed_dict={x:x_batch,y_: y_batch, keep_prob: 0.5})
        writer.add_summary(train, i+total*e)
    train_accuracy = sess.run(accuracy, feed_dict={x:x_batch,y_: y_batch, keep_prob: 0.5})

    print("epoch %d, training accuracy %g"%(e, train_accuracy))

test_accuracy = sess.run(accuracy, feed_dict={x:x_test[:10000],y_: y_test[:10000], keep_prob: 1.0})
print("test accuracy %g"%(test_accuracy))