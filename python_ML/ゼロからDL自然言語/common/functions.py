import tensorflow as tf
import numpy as np

def sigmoid(x):
    return 1 / (1 + tf.math.exp(-x))

def relu(x):
    return tf.dtypes.cast(tf.math.greater(x, 0), 'float') * x

def softmax(x):
    if x.ndim == 2:
        x = x - tf.math.reduce_max(x, axis=1, keepdims=True)
        x = tf.math.exp(x)
        x /= tf.math.reduce_sum(x, axis=1, keepdims=True)
    elif x.ndim == 1:
        x = x - tf.math.reduce_max(x, axis=0, keepdims=True)
        x = tf.math.exp(x) / tf.reduce_sum(tf.math.exp(x))
    return x

def cross_entropy_error(y, t):
    num_label = y.shape[0]
#     print(y.shape)
    if t.ndim == 1:
        t = tf.constant(np.identity(num_label)[t.numpy()], dtype='float')
    batch_size = y.shape[1]

    return -tf.reduce_sum(tf.math.log(y)*t) / batch_size
