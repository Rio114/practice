# coding: utf-8
import sys
sys.path.append('..')
import numpy as np
from common.time_layers import *


class SimpleRnnlm:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V, D, H = vocab_size, wordvec_size, hidden_size
        rn = tf.random.normal

        # 重みの初期化
        embed_W = tf.Variable(rn((V, D), dtype='float') / 100)
        rnn_Wx = tf.Variable(rn((D, H), dtype='float') / np.sqrt(D))
        rnn_Wh = tf.Variable(rn((H, H),  dtype='float') / np.sqrt(H))
        rnn_b = tf.Variable(tf.zeros(H, dtype='float'))
        affine_W = tf.Variable(rn((H, V), dtype='float') / np.sqrt(H))
        affine_b = tf.Variable(tf.zeros(V, dtype='float'))

        # レイヤの生成
        self.layers = [
            TimeEmbedding(embed_W),
            TimeRNN(rnn_Wx, rnn_Wh, rnn_b, stateful=True),
            TimeAffine(affine_W, affine_b)
        ]
        self.loss_layer = TimeSoftmaxWithLoss()
        self.rnn_layer = self.layers[1]

        # すべての重みと勾配をリストにまとめる
        self.params, self.grads = [], []
        for layer in self.layers:
            self.params += layer.params
            self.grads += layer.grads

    def forward(self, xs, ts):
        for layer in self.layers:
            xs = layer.forward(xs)
        loss = self.loss_layer.forward(xs, ts)
        return loss

    def backward(self, dout=1):
        dout = self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout

    def reset_state(self):
        self.rnn_layer.reset_state()
