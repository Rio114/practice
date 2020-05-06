import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization
from tensorflow.keras.layers import MaxPool2D, UpSampling2D, Dense
from tensorflow.keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam
import numpy as np

class SRGAN():
    def __init__(self, vgg_path, batch_size, input_shape=(270, 480, 3), tgt_shape=(1080, 1920, 3)):
        self.input_shape = input_shape
        self.batch_size = batch_size
        self.tgt_shape = tgt_shape
        self.vgg_path = vgg_path

        self.gen_net = []
        self.dis_net = []
        self.res_net = []

        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.vgg = self.build_vgg(vgg_path)

        self.disc_combined = self.build_disc_combined()
        self.vgg_combined = self.build_vgg_combined()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)

        self.disc_combined.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.vgg_combined.compile(loss='mean_squared_error', optimizer=self.optimizer)
        
    def build_generator(self, filters=64):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]

        # # Up 1
        layer_name = 'GU1'
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same',  name=layer_name+'_conv1', activation='relu'))    
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv2', activation='relu'))
    
        self.gen_net.append(UpSampling2D(size=(4,4), name=layer_name+'_upsamp'))
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutR', activation="sigmoid"))
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutG', activation="sigmoid"))
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutB', activation="sigmoid"))
        
        for i, l in enumerate(self.gen_net[:3]):
            layers.append(l(layers[i]))

        layers.append(self.gen_net[3](layers[-1]))
        layers.append(self.gen_net[4](layers[-2]))
        layers.append(self.gen_net[5](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        return Model(layers[0], layers[-1])

    def build_discriminator(self, filters=16):
        input_layer = Input(shape=self.tgt_shape)
        layers = [input_layer]
        
        # Down 0
        layer_name = 'DD0'
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu'))
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1', activation='relu'))
        self.dis_net.append(MaxPool2D(name=layer_name+'_pool'))#2, 3
        filters *= 2
    
        # Down 1
        layer_name = 'DD1'
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu'))
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1', activation='relu'))
        self.dis_net.append(MaxPool2D(name=layer_name+'_pool'))#2, 3
        filters *= 2
        
        # Down 2
        layer_name = 'DD2'
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu'))
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1', activation='relu'))
        self.dis_net.append(MaxPool2D(name=layer_name+'_pool'))#2, 3
        filters *= 2

        self.dis_net.append(Dropout(0.25))
        self.dis_net.append(Flatten())
        self.dis_net.append(BatchNormalization(momentum=0.8))
        self.dis_net.append(Dense(128, activation='sigmoid'))
        self.dis_net.append(Dense(64, activation='sigmoid'))
        self.dis_net.append(Dense(1, activation='sigmoid'))
        
        for i, l in enumerate(self.dis_net):
            layers.append(l(layers[i]))

        model = Model(layers[0], layers[-1])
        return model

    def build_vgg(self, vgg_path, l=10):
        vgg = load_model(self.vgg_path)
        model = Model(inputs=vgg.input, outputs=vgg.get_layer(vgg.layers[l].name).output)
        for l in model.layers:
            l.trainable = False
        return model

    def build_disc_combined(self):
        input_layer = Input(shape=self.input_shape)
        layers = [input_layer]

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        for i, l in enumerate(self.gen_net[:3]):
            layers.append(l(layers[i]))

        layers.append(self.gen_net[3](layers[-1]))
        layers.append(self.gen_net[4](layers[-2]))
        layers.append(self.gen_net[5](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        temp_num = len(layers)

        for i, l in enumerate(self.dis_net):
            layers.append(l(layers[i+temp_num-1]))

        return Model(layers[0], layers[-1])

    def build_vgg_combined(self):
        input_layer = Input(shape=self.input_shape)
        layers = [input_layer]

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        for i, l in enumerate(self.gen_net[:3]):
            layers.append(l(layers[i]))

        layers.append(self.gen_net[3](layers[-1]))
        layers.append(self.gen_net[4](layers[-2]))
        layers.append(self.gen_net[5](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        temp_num = len(layers)

        self.vgg.layers

        for i, l in enumerate(self.vgg.layers):
            layers.append(l(layers[i+temp_num-1]))

        return Model(layers[0], layers[-1])

    def train(self, X_low, X_high):
        batch_size = self.batch_size
        imgs_low = X_low
        imgs_high = X_high

        # -----------------
        # Training Discriminator
        # -----------------
        # print('training discriminator (true)...')
        d_loss_real = self.discriminator.train_on_batch(imgs_high, np.ones((batch_size, 1)))
        # print('training discriminator (false)...')
        d_loss_fake = self.disc_combined.train_on_batch(imgs_low, np.zeros((batch_size, 1)))
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # -----------------
        # Training Generator
        # -----------------
        # print('training generator...')
        hr_map = self.vgg.predict(imgs_high)
        vgg_map_low = self.vgg_combined.train_on_batch(imgs_low, hr_map)
        print('d_loss', d_loss)

