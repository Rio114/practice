import os
import sys
sys.path.append('../modules')
import argparse

import cv2
import numpy as np

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
# config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.8
session = InteractiveSession(config=config)

from gen_net import GEN

MODEL_PATH = '../models/20200515_generator.h5'
DATA_DIR = 'data/'

class SrImage():
    def __init__(self, data_dir=DATA_DIR):
        self.data_dir = data_dir

    def generate(self, image_file):
        '''
        input_path: test.jpg
        output_dir: output/directory/

        '''
        data_dir = self.data_dir
        if image_file.split('.')[-1] != 'jpg':
            return False

        input_path = data_dir + image_file
        output_file = image_file.split('.')[0] + '_r.jpg' 
        output_path = data_dir + output_file

        try:
            img = cv2.imread(input_path)
            shape = img.shape
            height = shape[0]
            width = shape[1]
            channel = shape[2]

            input_shape = (height, width, channel)
            gen = GEN(MODEL_PATH, input_shape)
            model = gen.generator

            pred = model.predict((img / 255)[np.newaxis, :, :, :])[0]
            out = (pred * 255).astype('u1')

        except:
            return False
            
        output = cv2.imwrite(output_path, out)
        if output:
            return output_file
        else:
            return False

def main():
    # parse path
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file", help="only for .jpg files")
    args = parser.parse_args()
    image_file = args.image_file
    
    obj = SrImage(DATA_DIR)
    obj.generate(image_file)

if __name__ == '__main__':
    main()