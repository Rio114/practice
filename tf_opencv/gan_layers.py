from keras.layers import Conv2D, UpSampling2D
from keras.layers import Input, Dense
from keras.layers import Reshape, Activation
from keras.layers import BatchNormalization
from keras.layers import Flatten
from keras.layers import LeakyReLU, Dropout
from keras.layers import ZeroPadding2D
from keras.models import Model
from keras.optimizers import Adam
import numpy as np

class gan_network():
    def __init__(self, z_dim, img_shape):
        self.z_dim = z_dim
        self.img_shape = img_shape
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.combined = self.build_combined()
        self.optimizer = Adam(lr=0.0002, beta_1=0.5)

        self.combined.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer)
        self.generator.compile(loss='binary_crossentropy', optimizer=self.optimizer)

        
    def build_generator(self):
        noise_shape = (None, self.z_dim)

        inputs = Input(shape=noise_shape)
        tensors = [inputs]
        self.gen_net = []

        self.gen_net.append(Dense(128 * 32 * 32, activation="relu"))
        self.gen_net.append(Reshape((32, 32, 128)))
        self.gen_net.append(BatchNormalization(momentum=0.8))
        self.gen_net.append(UpSampling2D())
        self.gen_net.append(Conv2D(128, kernel_size=3, padding="same"))
        self.gen_net.append(Activation("relu"))
        self.gen_net.append(BatchNormalization(momentum=0.8))
        self.gen_net.append(UpSampling2D())
        self.gen_net.append(Conv2D(64, kernel_size=3, padding="same"))
        self.gen_net.append(Activation("relu"))
        self.gen_net.append(BatchNormalization(momentum=0.8))
        self.gen_net.append(Conv2D(3, kernel_size=3, padding="same"))

        for i, l in enumerate(self.gen_net):
            tensors.append(l(tensors[i]))


        return Model(tensors[0], tensors[-1])
        
    def build_discriminator(self):
        inputs = Input(shape=self.img_shape)

        tensors = [inputs]

        self.disc_net = []
        self.disc_net.append(Conv2D(32, kernel_size=3, strides=2, padding="same"))
        self.disc_net.append(LeakyReLU(alpha=0.2))
        self.disc_net.append(Dropout(0.25))
        self.disc_net.append(Conv2D(64, kernel_size=3, strides=2, padding="same"))
        self.disc_net.append(ZeroPadding2D(padding=((0, 1), (0, 1))))
        self.disc_net.append(LeakyReLU(alpha=0.2))
        self.disc_net.append(Dropout(0.25))
        self.disc_net.append(BatchNormalization(momentum=0.8))
        self.disc_net.append(Conv2D(128, kernel_size=3, strides=2, padding="same"))
        self.disc_net.append(LeakyReLU(alpha=0.2))
        self.disc_net.append(Dropout(0.25))
        self.disc_net.append(BatchNormalization(momentum=0.8))
        self.disc_net.append(Conv2D(256, kernel_size=3, strides=1, padding="same"))
        self.disc_net.append(LeakyReLU(alpha=0.2))
        self.disc_net.append(Dropout(0.25))
        self.disc_net.append(Flatten())
        self.disc_net.append(Dense(1, activation='sigmoid'))

        for i, l in enumerate(self.disc_net):
            tensors.append(l(tensors[i]))

        return Model(tensors[0], tensors[-1])
    
    def set_combine_trainable(self):
        layers = self.discriminator.layers
        for l in layers:
            l.trainable = True

    def unset_combine_trainable(self):
        layers = self.discriminator.layers
        for l in layers:
            l.trainable = False

    def build_combined(self):
        noise_shape = (None, self.z_dim)

        inputs = Input(shape=noise_shape)
        tensors = [inputs]

        self.num_gen = len(self.gen_net)
        self.num_disc = len(self.disc_net)

        for i, l in enumerate(self.gen_net):
            tensors.append(l(tensors[i]))

        for i, l in enumerate(self.disc_net):
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