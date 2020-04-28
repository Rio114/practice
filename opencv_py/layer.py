from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization


class UNET():
    def __init__(self, input_shape=(240, 426, 3), tgt_shape=(720, 1280, 3)):
        self.input_shape = input_shape
        self.tgt_shape = tgt_shape

    def down(self, input_layer, filters, pool=True):
        conv1 = Conv2D(filters, (3, 3), padding='same', activation='relu')(input_layer)
        residual = Conv2D(filters, (3, 3), padding='same', activation='relu')(conv1)
        if pool:
            max_pool = MaxPooling2D()(residual)
            return max_pool, residual
        else:
            return residual

    def up_res(self, input_layer, residual, filters):
        filters= int(filters)
        upsample = UpSampling2D()(input_layer)
        upconv = Conv2D(filters, kernel_size=(2, 2), padding="same")(upsample)
        concat = Concatenate(axis=3)([residual, upconv])
        conv1 = Conv2D(filters, (3, 3), padding='same', activation='relu')(concat)    
        conv2 = Conv2D(filters, (3, 3), padding='same', activation='relu')(conv1)
        return conv2
    
    def up_only(self, input_layer, filters):
        filters= int(filters)
        upsample = UpSampling2D()(input_layer)
        upconv = Conv2D(filters, kernel_size=(2, 2), padding="same")(upsample)
        conv1 = Conv2D(filters, (3, 3), padding='same', activation='relu')(upconv)    
        conv2 = Conv2D(filters, (3, 3), padding='same', activation='relu')(conv1)
        return conv2

    def unet(self, num_filter=64):
        input_layer = Input(shape = self.input_shape)
        layers = [input_layer]
        residuals = []

        # Down 1, 64
        down1, res1 = self.down(input_layer, num_filter)
        residuals.append(res1)
        num_filter *= 2

#         # Down 2, 128
#         down2, res2 = self.down(down1, num_filter)
#         residuals.append(res1)
#         num_filter *= 2

        # Down 3, 8
        down3 = self.down(down1, num_filter, pool=False)

        # Up 1, 128
        num_filter /= 2
        up1 = self.up_res(down3, residual=residuals[-1], filters=num_filter)

        # Up 2, 64
        num_filter /= 2
#         up2 = self.up_only(up1, filters=num_filter)
        up3 = UpSampling2D(size=(3,3))(up1)
        out = Conv2D(filters=1, kernel_size=(1, 1), activation="sigmoid")(up3)
        model = Model(input_layer, out)

        return model
