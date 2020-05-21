from keras.models import Model, load_model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense, Add, Activation, LeakyReLU
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.engine.network import Network

import numpy as np

class SRGAN():
    def __init__(self, vgg_path, batch_size, input_shape=(45, 80, 3), tgt_shape=(135, 240, 3)):
        self.input_shape = input_shape
        self.tgt_shape = tgt_shape
        self.vgg_path = vgg_path
        self.batch_size = batch_size

        self.gen_net = []
        self.dis_net = []
        self.res_net = []

        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.vgg = self.build_vgg(vgg_path)

        self.disc_combined = self.build_disc_combined()
        self.vgg_combined = self.build_vgg_combined()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)

        self.generator.compile(loss='mean_squared_error', optimizer=self.optimizer)
        self.disc_combined.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.vgg_combined.compile(loss='mean_squared_error', optimizer=self.optimizer)

    def __add_conv_gen(self, layer_name, filters):
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act0'))
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm1'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act1'))

    def __add_conv_disc(self, layer_name, filters):
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0'))
        self.dis_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(LeakyReLU(name=layer_name+'_act0'))
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1'))
        self.dis_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm1'))
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

    def build_discriminator(self, filters=8):
        input_layer = Input(shape=self.tgt_shape)
        layers = [input_layer]
        
        # Down 0
        layer_name = 'DD0' #0~7
        self.__add_conv_disc(layer_name, filters)
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))        
        filters *= 2

        # Down 1
        layer_name = 'DD1' #8~13
        self.__add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))
        filters *= 2

        # Down 2
        layer_name = 'DD2' #8~13
        self.__add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))
        filters *= 2

        # Down 3
        layer_name = 'DD3' #8~13
        self.__add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))

        self.dis_net.append(Dropout(0.25))
        self.dis_net.append(BatchNormalization(momentum=0.8))
        self.dis_net.append(Flatten())
        self.dis_net.append(Dense(1024))
        self.dis_net.append(BatchNormalization(momentum=0.8))
        self.dis_net.append(LeakyReLU())
        self.dis_net.append(Dense(1, activation='sigmoid'))
        
        # body first up
        for i, operator in enumerate(self.dis_net):
            layers.append(operator(layers[i]))

        self.shared_discriminator = Network(input=layers[0], output=layers[-1], name='discriminator')
        model = Model(layers[0], layers[-1])
        return model

    def build_vgg(self, vgg_path, loss_layer=12):
        vgg = load_model(self.vgg_path)
        self.shared_vgg = Network(inputs=vgg.input, outputs=vgg.get_layer(vgg.layers[loss_layer].name).output, name='vgg')
        input_layer = Input(shape=self.tgt_shape)
        out = self.shared_vgg(input_layer)
        model = Model(input_layer, out)
        for l in model.layers:
            l.trainable = False
        return model

    def build_disc_combined(self):
        input_layer = Input(shape=self.input_shape)

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        gen = self.shared_generator(input_layer)
        out = self.shared_discriminator(gen)

        return Model(input_layer, out)

    def build_vgg_combined(self):
        input_layer = Input(shape=self.input_shape)
        layers = [input_layer]

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        gen = self.shared_generator(input_layer)
        out = self.shared_vgg(gen)

        return Model(input_layer, out)

    def train(self, X_low, X_high):
        batch_size = self.batch_size
        imgs_low = X_low
        imgs_high = X_high

        # -----------------
        # Training Discriminator
        # -----------------
        d_loss_real = self.discriminator.train_on_batch(imgs_high, np.ones((batch_size, 1)))
        d_loss_fake = self.disc_combined.train_on_batch(imgs_low, np.zeros((batch_size, 1)))

        # -----------------
        # Training Generator
        # -----------------
        hr_map = self.vgg.predict(imgs_high)
        vgg_loss = self.vgg_combined.train_on_batch(imgs_low, hr_map)

        # print(f'd_loss_real:{d_loss_real}, d_loss_fake:{d_loss_fake}, vgg_loss:{vgg_loss}')

    def valid(self, X_low, X_high):
        batch_size = self.batch_size
        imgs_low = X_low
        imgs_high = X_high

        # -----------------
        # Training Discriminator
        # -----------------
        d_loss_real = self.discriminator.test_on_batch(imgs_high, np.ones((batch_size, 1)))
        d_loss_fake = self.disc_combined.test_on_batch(imgs_low, np.zeros((batch_size, 1)))

        # -----------------
        # Training Generator
        # -----------------
        hr_map = self.vgg.predict(imgs_high)
        vgg_loss = self.vgg_combined.test_on_batch(imgs_low, hr_map)
        
        print(f'd_loss_real:{d_loss_real}, d_loss_fake:{d_loss_fake}, vgg_loss:{vgg_loss}')


