from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Input, Dense
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization

from ssd_layer import DefaultBox

class SSD_CNN():
    def __init__(self, num_classes, img_size=(300,300,3)):
        self.img_size = img_size
        self.num_classes = num_classes
        self.dim_box = 4 #(cx, cy, w, h)

    def CNN(self, train_class=2):
        """
        """

        ## Input
        self.inputs = Input(shape=self.img_size, name='input')

        ## Block 1
        self.conv1 = Conv2D(64, (3, 3),activation='relu',padding='same',name='conv1')(self.inputs)
        self.pool1 = MaxPooling2D((3,3),strides=(3, 3),padding='same',name='pool1')(self.conv1)

        ## Block 2
        self.conv2 = Conv2D(128, (3, 3),activation='relu',padding='same',name='conv2')(self.pool1)
        self.pool2 = MaxPooling2D((3, 3), strides=(3, 3), padding='same',name='pool2')(self.conv2)

        ## Block 3
        self.conv3 = Conv2D(256, (3, 3),activation='relu',padding='same',name='conv3')(self.pool2)
        self.pool3 = MaxPooling2D((3, 3), strides=(3, 3), padding='same',name='pool3')(self.conv3)

        ## Block 4
        self.conv4 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv4')(self.pool3)
        self.pool4 = MaxPooling2D((3, 3), strides=(3, 3), padding='same',name='pool4')(self.conv4)

        ## Block 4
        self.conv5 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv5')(self.pool4)
        self.pool5 = MaxPooling2D((3, 3), strides=(3, 3), padding='same',name='pool5')(self.conv5)

        self.flat = Flatten(name='flatten')(self.pool5)
        self.dense1 = Dense(1024, name='dense1')(self.flat)
        self.dense3 = Dense(256, name='dense3')(self.dense1)
        self.pred_cnn = Activation('softmax',name='pred_CNN')(self.dense3)
        return  Model(self.inputs, self.pred_cnn)

    def SSD(self):
        # detectors from layers

        self.detector_layers = [self.conv4, self.conv5]
        self.pred_SSD = self.detectors()
        return  Model(self.inputs, self.pred_SSD)

    def get_detector(self):
        return self.detector_layers
    
    def detectors(self):
        """
        layers: list of layer
        """
        mbox_loc_list = []
        mbox_conf_list = []
        mbox_defbox_list = []

        num_def = 6 
        aspect_ratios = [2, 3] # -> [1(min), 1((min*max)**0.5), 2, 3, 1/2, 1/3] by DefaultBox()
        
        for layer in self.detector_layers:

            name_layer = layer.name.split('/')[0] + '_' # eg. 'conv5_1/Relu:0'-> 'conv5_1'

            layer_mbox_loc = Conv2D(num_def*self.dim_box, (3, 3), padding='same',
                                    name='{}_mbox_loc'.format(name_layer))(layer)
            layer_length = layer_mbox_loc.shape[1].value
            layer_mbox_loc_flat = Flatten(name='{}_mbox_loc_flat'.format(name_layer))(layer_mbox_loc)
            layer_mbox_loc_norm = BatchNormalization(name='{}_mbox_loc_norm'.format(name_layer))(layer_mbox_loc_flat)
            mbox_loc_list.append(layer_mbox_loc_norm)
            
            layer_mbox_conf = Conv2D(num_def*self.num_classes, (3, 3), padding='same',
                                    name='{}_mbox_conf'.format(name_layer))(layer)
            layer_mbox_conf_flat = Flatten(name='{}_mbox_conf_flat'.format(name_layer))(layer_mbox_conf)

            layer_mbox_conf_norm = BatchNormalization(name='{}_mbox_conf_norm'.format(name_layer))(layer_mbox_conf_flat)
            mbox_conf_list.append(layer_mbox_conf_norm)
            
            layer_mbox_defbox = DefaultBox(self.img_size,
                                        self.img_size[0]/layer_length*0.8,
                                        self.img_size[0]/layer_length,
                                        aspect_ratios=aspect_ratios,
                                        variances=[0.1, 0.1, 0.2, 0.2],
                                        name='{}_mbox_defbox'.format(name_layer))(layer)
            mbox_defbox_list.append(layer_mbox_defbox)
            
        mbox_loc = Concatenate(name='mbox_loc', axis=1)(mbox_loc_list)
        num_boxes = mbox_loc._keras_shape[-1] // 4
        mbox_loc = Reshape((num_boxes, self.dim_box),name='mbox_loc_final')(mbox_loc)

        mbox_conf = Concatenate(name='mbox_conf', axis=1)(mbox_conf_list)
        mbox_conf = Reshape((num_boxes, self.num_classes),name='mbox_conf_logits')(mbox_conf)
        mbox_conf = Activation('softmax',name='mbox_conf_final')(mbox_conf)
        
        mbox_defbox = Concatenate(name='mbox_defbox',axis=1)(mbox_defbox_list)

        predictions = Concatenate(name='predictions',axis=2)([mbox_loc, mbox_conf, mbox_defbox])
        
        return predictions