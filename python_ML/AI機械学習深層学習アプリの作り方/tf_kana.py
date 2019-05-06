import tensorflow as tf 

INPUT_DIM = 100
OUTPUT_DIM = 10

x = tf.placeholder(tf.float32, [None, INPUT_DIM], 'INPUT')
t_= tf.placeholder(tf.float32, [None, OUTPUT_DIM], 'OUTPUT')

conv_1 = tf.nn.conv2d