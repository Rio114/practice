# coding: utf-8
import sys
sys.path.append('..')
import numpy as np
from common.layers import MatMul, SoftmaxWithLoss

class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size
        
        W_in = tf.Variable(tf.random.normal((V, H), mean=0.0, stddev=0.01, dtype='float'))
        W_out = tf.Variable(tf.random.normal((H, V), mean=0.0, stddev=0.01, dtype='float'))

        self.in_layer0 = MatMul(W_in)
        self.in_layer1 = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWithLoss()

        layers = [
                self.in_layer0,
                self.in_layer1,
                self.out_layer,
                self.loss_layer
        ]

        self.params = []
        self.grads = []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads
            
        self.word_vecs = W_in
        
    def forward(self, contexts, target):
        h0 = self.in_layer0.forward(contexts[:, 0])
        h1 = self.in_layer1.forward(contexts[:, 1])
        h = (h0 + h1) * 0.5
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)
        return loss
    
    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da *= 0.5
        self.in_layer1.backward(da)
        self.in_layer0.backward(da)
        
        self.grads = []
        layers = [
                self.in_layer0,
                self.in_layer1,
                self.out_layer,
                self.loss_layer
        ]
        
        for layer in layers:
            self.grads += layer.grads
        
        return None