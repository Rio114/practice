import os
import numpy as np
from PIL import Image
import random


class ImageDataGenerator(object):
    def __init__(self, input_dir, tgt_dir):
        self.input_dir = input_dir
        self.tgt_dir = tgt_dir
        self.img_list = os.listdir(input_dir)
        assert self.img_list == os.listdir(tgt_dir)
        self.reset()

    def reset(self):
        self.inputs = []
        self.targets = []

    def flow_from_directory(self, batch_size=16):
        train_imges = random.sample(self.img_list, batch_size)
        while True:
            for img in train_imges:
                input_path = input_dir + img
                tgt_path = tgt_dir + img

                X = (np.array(Image.open(input_path)) - 127.5) / 127.5
                Y = (np.array(Image.open(tgt_path)) - 127.5) / 127.5

                X_list.append(X.reshape([1, X.shape[0], X.shape[1], X.shape[2]]))
                Y_list.append(Y.reshape([1, Y.shape[0], Y.shape[1], Y.shape[2]]))
    
            inputs = np.vstack(X_list)
            targets = np.vstack(Y_list)

            yield inputs, targets