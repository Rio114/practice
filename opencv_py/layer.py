from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization

class UNET():
    def __init__(self, input_shape=(240, 426, 3), tgt_shape=(720, 1278, 3)):
        self.input_shape = input_shape
        self.tgt_shape = tgt_shape
        
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.combined = self.build_combined()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)

        self.combined.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.generator.compile(loss='binary_crossentropy', optimizer=self.optimizer)


    def down(self, input_layer, filters, layer_name, pool=True):
        conv = Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv', activation='relu')(input_layer)
        res = Conv2D(filters, (3, 3), padding='same', name=layer_name+'_res', activation='relu')(conv)
        if pool:
            max_pool = MaxPooling2D(name=layer_name+'_pool',)(res)
            return max_pool, res
        else:
            return res

    def up_res(self, input_layer, residual, filters, layer_name):
        filters= int(filters)
        upsample = UpSampling2D(name=layer_name+'_upsamp')(input_layer)
        upconv = Conv2D(filters, kernel_size=(2, 2), name=layer_name+'_upconv', padding="same")(upsample)
        concat = Concatenate(axis=3)([residual, upconv])
        conv1 = Conv2D(filters, (3, 3), padding='same',  name=layer_name+'_conv1', activation='relu')(concat)    
        conv2 = Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv2', activation='relu')(conv1)
        return conv2
    
    # def up_only(self, input_layer, filters, layer_name):
    #     filters= int(filters)
    #     upsample = UpSampling2D(name=layer_name+'_upsamp')(input_layer)
    #     upconv = Conv2D(filters, kernel_size=(2, 2), name=layer_name+'_upconv', padding="same")(upsample)
    #     conv1 = Conv2D(filters, (3, 3), padding='same',  name=layer_name+'_conv1', activation='relu')(upconv)    
    #     conv2 = Conv2D(filters, (3, 3), padding='same', name=layer_name+'_conv2', activation='relu')(conv1)
    #     return conv2

    def build_generator(self, num_filter=64):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]
        residuals = []

        # Down 1, 64
        down1, res1 = self.down(input_layer, num_filter, layer_name='GD1')
        residuals.append(res1)
        num_filter *= 2

        # Down 2, 8
        down2 = self.down(down1, num_filter, layer_name='GD2', pool=False)

        # Up 1, 128
        num_filter /= 2
        up1 = self.up_res(down2, residual=residuals[-1], layer_name='GU1', filters=num_filter)

        # Up 2, 64
        num_filter /= 2
        up2 = UpSampling2D(size=(3,3), name='GU2_upsamp')(up1)
        outR = Conv2D(filters=1, kernel_size=(1, 1), activation="sigmoid", name='GoutR')(up2)
        outG = Conv2D(filters=1, kernel_size=(1, 1), activation="sigmoid", name='GoutG')(up2)
        outB = Conv2D(filters=1, kernel_size=(1, 1), activation="sigmoid", name='GoutB')(up2)
        out  = Concatenate(axis=3)([outR, outG, outB])
        
        model = Model(input_layer, out)

        return model

    def build_discriminator(self, num_filter=16):
        inputs = Input(shape=self.tgt_shape)

        tensors = [inputs]
        # Down 1
        down1, _ = self.down(inputs, num_filter, layer_name='DD1')
        num_filter *= 2

        # Down 2
        down2, _ = self.down(down1, num_filter, layer_name='DD2')
        num_filter *= 2

        model = Model(input_layer, out)

        return model


    def set_combine_trainable(self):
        for l in self.discriminator.layers:
            l.trainable = True

    def unset_combine_trainable(self):
        for l in self.discriminator.layers:
            l.trainable = False

    def build_combined(self):
        inputs = Input(shape=self.input_shape)
        tensors = [inputs]

        self.num_gen = len(self.generator.layers)
        self.num_disc = len(self.discriminator.layers)

        for i, l in enumerate(self.generator.layers):
            tensors.append(l(tensors[i]))

        for i, l in enumerate(self.discriminator.layers):
            tensors.append(l(tensors[i+self.num_gen]))

        return Model(tensors[0], tensors[-1])

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
