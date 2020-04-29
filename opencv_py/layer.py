from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization
from keras.optimizers import Adam

class UNET():
    def __init__(self, input_shape=(240, 426, 3), tgt_shape=(720, 1278, 3)):
        self.input_shape = input_shape
        self.tgt_shape = tgt_shape

        self.gen_net = []
        self.dis_net = []
        self.res_net = []

        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.combined = self.build_combined()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)

        # self.combined.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        # self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        # self.generator.compile(loss='binary_crossentropy', optimizer=self.optimizer)

    def build_generator(self, filters=64):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]

        # Down 1
        layer_name = 'GD0'
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv', activation='relu')) #0, 1
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_res', activation='relu')) #1, 2
        self.gen_net.append(MaxPooling2D(name=layer_name+'_pool')) #2, 3
        filters *= 2
    
        # Down 2
        layer_name = 'GD1'
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv', activation='relu')) #3, 4
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_res', activation='relu')) #4, 5
        filters *= 2

        # Up 1
        layer_name = 'GU0'
        filter = int(filters / 2)
        self.gen_net.append(UpSampling2D(name=layer_name+'_upsamp')) #5
        self.gen_net.append(Conv2D(filters, kernel_size=(2, 2), name=layer_name+'_upconv', padding="same")) #6
        ## concat res
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same',  name=layer_name+'_conv1', activation='relu')) #7    
        self.gen_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv2', activation='relu')) #8
    
        # Up 2
        filter = int(filters / 2)
        layer_name = 'GU1'
        self.gen_net.append(UpSampling2D(size=(3,3), name=layer_name+'_upsamp')) #9
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutR', activation="sigmoid")) #10
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutG', activation="sigmoid")) #11
        self.gen_net.append(Conv2D(filters=1, kernel_size=(3, 3), padding='same', name='GoutB', activation="sigmoid")) #12
        
        for i, l in enumerate(self.gen_net[:7]):
            layers.append(l(layers[i]))

        layers.append(Concatenate(axis=3)([layers[2], layers[-1]]))
        
        for i, l in enumerate(self.gen_net[7:10]):
            layers.append(l(layers[i+7]))

        layers.append(self.gen_net[10](layers[-1]))
        layers.append(self.gen_net[11](layers[-2]))
        layers.append(self.gen_net[12](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        return Model(layers[0], layers[-1])

    def build_discriminator(self, filters=16):
        input_layer = Input(shape=self.tgt_shape)
        layers = [input_layer]
        # Down 1
        layer_name = 'DD0'
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu')) #0, 1
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1', activation='relu')) #1, 2
        self.dis_net.append(MaxPooling2D(name=layer_name+'_pool')) #2, 3
        filters *= 2
    
        # Down 2
        layer_name = 'DD1'
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv0', activation='relu')) #3, 4
        self.dis_net.append(Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv1', activation='relu')) #4, 5
        
        for i, l in enumerate(self.dis_net):
            layers.append(l(layers[i]))

        model = Model(layers[0], layers[-1])
        return model

    def set_combine_trainable(self):
        for l in self.discriminator.layers:
            l.trainable = True

    def unset_combine_trainable(self):
        for l in self.discriminator.layers:
            l.trainable = False

    def build_combined(self):
        input_layer = Input(shape=self.input_shape)
        layers = [input_layer]

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        for i, l in enumerate(self.gen_net[:7]):
            layers.append(l(layers[i]))

        layers.append(Concatenate(axis=3)([layers[2], layers[-1]]))
        
        for i, l in enumerate(self.gen_net[7:10]):
            layers.append(l(layers[i+7]))

        layers.append(self.gen_net[10](layers[-1]))
        layers.append(self.gen_net[11](layers[-2]))
        layers.append(self.gen_net[12](layers[-3]))

        layers.append(Concatenate(axis=3)([layers[-3], layers[-2], layers[-1]]))

        temp_num = len(layers)

        for i, l in enumerate(self.dis_net):
            layers.append(l(layers[i+temp_num-1]))

        return Model(layers[0], layers[-1])

    def train(self, X_train, epochs, batch_size=128):
        half_batch = int(batch_size / 2)
        X_train = (X_train.astype(np.float32) - 127.5) / 127.5

        for epoch in range(epochs):
            idx = np.random.randint(0, X_train.shape[0], half_batch)
            imgs = X_train[idx]
            noise = np.random.uniform(-1, 1, (half_batch, 1, self.z_dim))

            # -----------------
            # Training Discriminator
            # -----------------
            self.set_combine_trainable()
            gen_imgs = self.generator.predict(noise)
            d_loss_real = self.discriminator.train_on_batch(imgs, np.ones((half_batch, 1)))
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, np.zeros((half_batch, 1)))
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            # -----------------
            # Training Generator
            # -----------------
            self.unset_combine_trainable()
            noise = np.random.uniform(-1, 1, (batch_size, 1, self.z_dim))
            g_loss = self.combined.train_on_batch(noise, np.ones((batch_size, 1)))

            print("Epoch:%d" % epoch)
