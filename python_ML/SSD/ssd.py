from keras.models import Model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Reshape
from keras.layers import Activation
from keras.layers import concatenate
from keras.layers import Dropout

from ssd_layer import DefaultBox

class SSD():
    def __init__(self, num_classes, img_size=(300,300,3)):
        self.img_size = img_size
        self.num_classes = num_classes
        self.dim_box = 4 #(cx, cy, w, h)

    def base_CNN(self, train_class=2):
        """
        """

        ## Input
        self.inputs = Input(shape=self.img_size, name='input')

        ## Block 1
        self.conv1_1 = Conv2D(64, (3, 3),activation='relu',padding='same',name='conv1_1')(self.inputs)
        self.conv1_2 = Conv2D(64, (3, 3),activation='relu',padding='same',name='conv1_2')(self.conv1_1)
        self.pool1 = MaxPooling2D((2,2),strides=(2,2),padding='same',name='pool1')(self.conv1_2)

        ## Block 2
        self.conv2_1 = Conv2D(128, (3, 3),activation='relu',padding='same',name='conv2_1')(self.pool1)
        self.conv2_2 = Conv2D(128, (3, 3),activation='relu',padding='same',name='conv2_2')(self.conv2_1)
        self.pool2 = MaxPooling2D((2, 2), strides=(2, 2), padding='same',name='pool2')(self.conv2_2)

        ## Block 3
        self.conv3_1 = Conv2D(256, (3, 3),activation='relu',padding='same',name='conv3_1')(self.pool2)
        self.conv3_2 = Conv2D(256, (3, 3),activation='relu',padding='same',name='conv3_2')(self.conv3_1)
        self.conv3_3 = Conv2D(256, (3, 3),activation='relu',padding='same',name='conv3_3')(self.conv3_2)
        self.pool3 = MaxPooling2D((2, 2), strides=(2, 2), padding='same',name='pool3')(self.conv3_3)

        ## Block 4
        self.conv4_1 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv4_1')(self.pool3)
        self.conv4_2 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv4_2')(self.conv4_1)
        self.conv4_3 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv4_3')(self.conv4_2)
        self.pool4 = MaxPooling2D((2, 2), strides=(2, 2), padding='same',name='pool4')(self.conv4_3)

        ## Block 5
        self.conv5_1 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv5_1')(self.pool4)
        self.conv5_2 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv5_2')(self.conv5_1)
        self.conv5_3 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv5_3')(self.conv5_2)
        self.pool5 = MaxPooling2D((2, 2), strides=(2, 2), padding='same',name='pool5')(self.conv5_3)

        ## FC6
        self.fc6 = Conv2D(1024, (3, 3), dilation_rate=(6, 6),activation='relu', padding='same',name='fc6')(self.pool2)

        ## FC7
        self.fc7 = Conv2D(1024, (1, 1), activation='relu',padding='same',name='fc7')(self.fc6)

        ## Block 6
        self.conv6_1 = Conv2D(256, (1, 1),activation='relu',padding='same',name='conv6_1')(self.fc7)
        self.conv6_2 = Conv2D(512, (3, 3),activation='relu',padding='same',name='conv6_2')(self.conv6_1)

        ## Block 7
        self.conv7_1 = Conv2D(128, (1, 1),activation='relu',padding='same',name='conv7_1')(self.conv6_2)
        self.conv7_2 = Conv2D(256, (3, 3),strides=(2,2),activation='relu',padding='valid',name='conv7_2')(self.conv7_1)

        ## Block 8
        self.conv8_1 = Conv2D(128, (1, 1),activation='relu',padding='same',name='conv8_1')(self.conv7_2)
        self.conv8_2 = Conv2D(256, (3, 3),strides=(2,2),activation='relu',padding='same',name='conv8_2')(self.conv8_1)

        # Last Pool
        self.pool6 = GlobalAveragePooling2D(name='pool6')(self.conv8_2)

        self.flat = Flatten(name='flatten')(self.conv8_2)
        self.dense1 = Dense(self.num_classes, name='dense1')(self.flat)
        self.drop = Dropout(0.5, name='drop')(self.dense1)
        self.dense2 = Dense(train_class, name='dense2')(self.drop)
        self.pred_CNN = Activation('softmax',name='pred_CNN')(self.dense2)
        return  Model(self.inputs, self.pred_CNN)

    def SSD(self):
        # detectors from layers
        self.detector_layers = [self.conv4_3, self.conv6_2, self.conv7_2]
        self.pred_SSD = self.detectors()
        return  Model(self.inputs, self.pred_SSD)

    def get_detector(self):
        return self.detector_layers
    
    def detectors(self):
        """
        layers: list of layer
        to learn weight for any num_classes, additional '_' is in mbox layer names.
        """
        mbox_loc_list = []
        mbox_conf_list = []
        mbox_defbox_list = []

        num_def = 6 
        aspect_ratios = [2, 3] # -> [1(min), 1((min*max)**0.5), 2, 3, 1/2, 1/3] by DefaultBox()
        
        for layer in self.detector_layers:

            name_layer = layer.name.split('/')[0] + '_' # eg. 'conv5_1/Relu:0'-> 'conv5_1'

            layer_mbox_loc = Conv2D(num_def * self.dim_box,(3,3),padding='same',
                                    name='{}_mbox_loc'.format(name_layer))(layer)
            layer_length = layer_mbox_loc.shape[1].value
            layer_mbox_loc_flat = Flatten(name='{}_mbox_loc_flat'.format(name_layer))(layer_mbox_loc)
            mbox_loc_list.append(layer_mbox_loc_flat)
            
            layer_mbox_conf = Conv2D(num_def * self.num_classes,(3,3),padding='same',
                                    name='{}_mbox_conf'.format(name_layer))(layer)
            layer_mbox_conf_flat = Flatten(name='{}_mbox_conf_flat'.format(name_layer))(layer_mbox_conf)
            mbox_conf_list.append(layer_mbox_conf_flat)
            
            layer_mbox_defbox = DefaultBox(self.img_size,
                                        self.img_size[0]/layer_length*0.8,
                                        self.img_size[0]/layer_length,
                                        aspect_ratios=aspect_ratios,
                                        variances=[0.1, 0.1, 0.1, 0.1],
                                        name='{}_mbox_defbox'.format(name_layer))(layer)
            mbox_defbox_list.append(layer_mbox_defbox)
            
        mbox_loc = concatenate(mbox_loc_list, name='mbox_loc', axis=1)
        num_boxes = mbox_loc._keras_shape[-1] // 4
        mbox_loc = Reshape((num_boxes, self.dim_box),name='mbox_loc_final')(mbox_loc)

        mbox_conf = concatenate(mbox_conf_list,name='mbox_conf', axis=1)
        mbox_conf = Reshape((num_boxes, self.num_classes),name='mbox_conf_logits')(mbox_conf)
        mbox_conf = Activation('softmax',name='mbox_conf_final')(mbox_conf)
        
        mbox_defbox = concatenate(mbox_defbox_list,name='mbox_defbox',axis=1)

        predictions = concatenate([mbox_loc, mbox_conf, mbox_defbox], name='predictions',axis=2)
        
        return predictions