import os
import numpy as np
import cv2
import random

class ImageDataGenerator(object):
    def __init__(self, input_dir, tgt_dir, batch_size):
        self.input_dir = input_dir
        self.tgt_dir = tgt_dir
        self.batch_size = batch_size
        self.img_list = os.listdir(input_dir)
        assert self.img_list == os.listdir(tgt_dir)
        self.reset()

    def reset(self):
        self.inputs = []
        self.targets = []

    def flow_from_directory(self):
        batch_size = self.batch_size
        while True:
            X_list = []
            Y_list = []
            train_imges = random.sample(self.img_list, batch_size)
            for img in train_imges:
                input_path = self.input_dir + img
                tgt_path = self.tgt_dir + img

                X = np.array(cv2.imread(input_path), dtype='u1') 
                Y = np.array(cv2.imread(tgt_path), dtype='u1')

                X_list.append(X.reshape([1, X.shape[0], X.shape[1], X.shape[2]]))
                Y_list.append(Y.reshape([1, Y.shape[0], Y.shape[1], Y.shape[2]]))
    
            inputs  = np.vstack(X_list)
            inputs  = ((inputs - 127.5)/ 127.5).astype('f4')

            targets = np.vstack(Y_list)
            targets  = ((targets - 127.5)/ 127.5).astype('f4')

            yield inputs, targets