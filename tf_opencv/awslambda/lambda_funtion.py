import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
import numpy as np

from keras.models import Model, load_model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense, Add, Activation, LeakyReLU
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.engine.network import Network

s3_client = boto3.client('s3')
MODEL_PATH = '../models/20200522_generator.h5'

class GEN():
    def __init__(self, model_path, input_shape=(45, 80, 3)):
        self.input_shape = input_shape
        self.gen_net = []
        self.generator = self.build_generator()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)
        self.generator.compile(loss='mean_squared_error', optimizer=self.optimizer)
        self.generator.load_weights(model_path)

    def __add_conv_gen(self, layer_name, filters):
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act0'))
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm1'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act1'))
    def build_generator(self, filters=128):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]

        # define operators
        layer_name = 'G_Head' # 0~2
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act0'))

        layer_name = 'G_Body_0' # 3~8
        self.__add_conv_gen(layer_name, filters)

        layer_name = 'G_Body_1' # 9~14
        self.__add_conv_gen(layer_name, filters)

        layer_name = "G_Up_1" # 15
        self.gen_net.append(UpSampling2D(size=(2,2), name=layer_name+'_upsamp'))

        layer_name = 'G_Body_3' # 16~21
        self.__add_conv_gen(layer_name, filters)

        layer_name = "G_Tail" # 22~23
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(Conv2D(filters=3, kernel_size=(3, 3), padding='same', name='outRGB', activation="sigmoid"))

        # build network
        # head
        num = len(layers)
        for i, operator in enumerate(self.gen_net[:3]):
            layers.append(operator(layers[i+num-1]))
        head_out = layers[-1]

        # body first 0
        num = len(layers)
        for i, operator in enumerate(self.gen_net[3:9]):
            layers.append(operator(layers[i+num-1]))
        layers.append(Add()([layers[-1], head_out]))
        body_0_out = layers[-1]

        # body first 1
        num = len(layers)
        for i, operator in enumerate(self.gen_net[9:15]):
            layers.append(operator(layers[i+num-1]))
        layers.append(Add()([layers[-1], body_0_out]))
        body_1_out = layers[-1]

        layers.append(Add()([head_out, body_1_out]))

        # up
        layers.append(self.gen_net[15](layers[-1]))

        # tail
        prior_tail = layers[-1]
        num = len(layers)
        for i, operator in enumerate(self.gen_net[16:22]):
            layers.append(operator(layers[i+num-1]))
        layers.append(Add()([layers[-1], prior_tail]))

        layers.append(self.gen_net[-2](layers[-1])) # batch_norm
        layers.append(self.gen_net[-1](layers[-1])) # rgb

        self.shared_generator = Network(input=layers[0], output=layers[-1], name='generator')
        return Model(layers[0], layers[-1])

def sr_image(img_path, out_path):
    im = Image.open(img_path)
    w = im.width
    h = im.height
    img = np.array(im)[:, :, ::-1]
    input_shape = (h, w, 3)
    model_path = MODEL_PATH

    gen = GEN(model_path, input_shape)

    model = gen.generator
    pred = model.predict((img / 255)[np.newaxis, :, :, :])[0]
    out = (pred * 255).astype('u1')
    out_pil = out[:, :, ::-1]
    new_image = Image.fromarray(out_pil)
    new_image.save(out_path)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        splitkey = key.split('/')
        newkey = key.replace(splitkey[0], 'outputs')
        tmpkey = key.replace('/', '')
        download_path = f'/tmp/{uuid.uuid4()}{tmpkey}'
        upload_path = f'/tmp/resized-{tmpkey}'
        s3_client.download_file(bucket, key, download_path)
        sr_image(download_path, upload_path)
        s3_client.upload_file(upload_path, bucket, newkey)

def main():
    img_path = 'original.jpg'
    out_path = 'sr_image.jpg'
    sr_image(img_path, out_path)

if __name__ == "__main__":
    main()
