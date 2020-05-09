from keras.models import Model, load_model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense, Add, Activation
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization
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
    
    def add_conv_gen(self, layer_name, filters):
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.gen_net.append(Activation(activation='relu', name=layer_name+'_act0'))
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1'))
        self.gen_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm1'))
        self.gen_net.append(Activation(activation='relu', name=layer_name+'_act1'))

    def add_conv_disc(self, layer_name, filters):
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0'))
        self.dis_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm0'))
        self.dis_net.append(Activation(activation='relu', name=layer_name+'_act0'))
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1'))
        self.dis_net.append(BatchNormalization(momentum=0.8, name=layer_name+'_norm1'))
        self.dis_net.append(Activation(activation='relu', name=layer_name+'_act1'))   

    def build_generator(self, filters=64):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]
        
        # define operators
        layer_name = 'G_Head' # 0
        self.gen_net.append(Conv2D(filters, (9, 9), padding='same', name=layer_name+'_conv0', activation='relu'))    
        
        layer_name = 'G_Body_0' # 1~6
        self.add_conv_gen(layer_name, filters)   

        layer_name = 'G_Body_1' # 7~12
        self.add_conv_gen(layer_name, filters)

        layer_name = "G_Up_1" # 13
        self.gen_net.append(UpSampling2D(size=(2,2), name=layer_name+'_upsamp'))

        layer_name = 'G_Body_2' # 14~19
        self.add_conv_gen(layer_name, filters)

        layer_name = 'G_Body_3' # 20~25
        self.add_conv_gen(layer_name, filters)

        layer_name = "G_Up_2" # 26
        self.gen_net.append(UpSampling2D(size=(2,2), name=layer_name+'_upsamp'))

        layer_name = 'G_Body_4' # 27~32
        self.add_conv_gen(layer_name, filters)

        layer_name = "G_Tail"
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutR', activation="sigmoid"))
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutG', activation="sigmoid"))
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutB', activation="sigmoid"))
        
        # build network
        # head
        operator = self.gen_net[0]
        layers.append(operator(layers[0]))
        head_out = layers[-1] 

        # body first up
        num = len(layers)
        for i, operator in enumerate(self.gen_net[1:6]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[6]
        layers.append(Add()([operator(layers[-1]), head_out]))
        body_0_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[7:12]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[12]
        layers.append(Add()([operator(layers[-1]), body_0_out]))
        body_1_out = layers[-1]

        layers.append(Add()(([head_out, body_1_out])))
        layers.append(self.gen_net[13](layers[-1]))

        # body second up
        num = len(layers)
        prior_up_2 = layers[-1]
        for i, operator in enumerate(self.gen_net[14:19]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[19]
        layers.append(Add()([operator(layers[-1]), prior_up_2]))
        body_2_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[20:25]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[25]
        layers.append(Add()([operator(layers[-1]), body_2_out]))
        body_3_out = layers[-1]

        layers.append(Add()(([prior_up_2, body_3_out])))
        layers.append(self.gen_net[26](layers[-1]))

        # tail
        num = len(layers)
        prior_rgb = layers[-1]
        for i, operator in enumerate(self.gen_net[27:32]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[32]
        layers.append(Add()([operator(layers[-1]), prior_rgb]))

        prior_up = layers[-1]
        layers.append(self.gen_net[-4](prior_up))
        layers.append(self.gen_net[-3](layers[-1]))
        layers.append(self.gen_net[-2](layers[-2]))
        layers.append(self.gen_net[-1](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        return Model(layers[0], layers[-1])

    def build_discriminator(self, filters=16):
        input_layer = Input(shape=self.tgt_shape)
        layers = [input_layer]
        
        # Down 0
        layer_name = 'DD0'
        self.add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))        
    
        # Down 1
        layer_name = 'DD1'
        self.add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))        
        
        # Down 2
        layer_name = 'DD2'
        self.add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))

        # Down 3
        layer_name = 'DD3'
        self.add_conv_disc(layer_name, filters)   
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool'))       

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

 # build network
        # head
        operator = self.gen_net[0]
        layers.append(operator(layers[0]))
        head_out = layers[-1] 

        # body first up
        num = len(layers)
        for i, operator in enumerate(self.gen_net[1:6]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[6]
        layers.append(Add()([operator(layers[-1]), head_out]))
        body_0_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[7:12]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[12]
        layers.append(Add()([operator(layers[-1]), body_0_out]))
        body_1_out = layers[-1]

        layers.append(Add()(([head_out, body_1_out])))
        layers.append(self.gen_net[13](layers[-1]))

        # body second up
        num = len(layers)
        prior_up_2 = layers[-1]
        for i, operator in enumerate(self.gen_net[14:19]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[19]
        layers.append(Add()([operator(layers[-1]), prior_up_2]))
        body_2_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[20:25]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[25]
        layers.append(Add()([operator(layers[-1]), body_2_out]))
        body_3_out = layers[-1]

        layers.append(Add()(([prior_up_2, body_3_out])))
        layers.append(self.gen_net[26](layers[-1]))

        # tail
        num = len(layers)
        prior_rgb = layers[-1]
        for i, operator in enumerate(self.gen_net[27:32]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[32]
        layers.append(Add()([operator(layers[-1]), prior_rgb]))

        prior_up = layers[-1]
        layers.append(self.gen_net[-4](prior_up))
        layers.append(self.gen_net[-3](layers[-1]))
        layers.append(self.gen_net[-2](layers[-2]))
        layers.append(self.gen_net[-1](layers[-3]))

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

 # build network
        # head
        operator = self.gen_net[0]
        layers.append(operator(layers[0]))
        head_out = layers[-1] 

        # body first up
        num = len(layers)
        for i, operator in enumerate(self.gen_net[1:6]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[6]
        layers.append(Add()([operator(layers[-1]), head_out]))
        body_0_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[7:12]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[12]
        layers.append(Add()([operator(layers[-1]), body_0_out]))
        body_1_out = layers[-1]

        layers.append(Add()(([head_out, body_1_out])))
        layers.append(self.gen_net[13](layers[-1]))

        # body second up
        num = len(layers)
        prior_up_2 = layers[-1]
        for i, operator in enumerate(self.gen_net[14:19]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[19]
        layers.append(Add()([operator(layers[-1]), prior_up_2]))
        body_2_out = layers[-1]

        num = len(layers)
        for i, operator in enumerate(self.gen_net[20:25]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[25]
        layers.append(Add()([operator(layers[-1]), body_2_out]))
        body_3_out = layers[-1]

        layers.append(Add()(([prior_up_2, body_3_out])))
        layers.append(self.gen_net[26](layers[-1]))

        # tail
        num = len(layers)
        prior_rgb = layers[-1]
        for i, operator in enumerate(self.gen_net[27:32]):
            layers.append(operator(layers[i+num-1]))
        operator = self.gen_net[32]
        layers.append(Add()([operator(layers[-1]), prior_rgb]))

        prior_up = layers[-1]
        layers.append(self.gen_net[-4](prior_up))
        layers.append(self.gen_net[-3](layers[-1]))
        layers.append(self.gen_net[-2](layers[-2]))
        layers.append(self.gen_net[-1](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        temp_num = len(layers)

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
        d_loss_real = self.discriminator.train_on_batch(imgs_high, np.ones((batch_size, 1)))
        d_loss_fake = self.disc_combined.train_on_batch(imgs_low, np.zeros((batch_size, 1)))
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # -----------------
        # Training Generator
        # -----------------
        hr_map = self.vgg.predict(imgs_high)
        vgg_map_low = self.vgg_combined.train_on_batch(imgs_low, hr_map)
        print('d_loss', d_loss)

