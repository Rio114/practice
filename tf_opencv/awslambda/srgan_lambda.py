
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import boto3
import argparse
import os
import re
import tempfile

import cv2
import numpy as np
from six.moves import urllib

from keras.models import Model, load_model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, Dense, Add, Activation, LeakyReLU
from keras.layers import Flatten, Reshape, Activation, Concatenate, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.engine.network import Network

s3 = boto3.resource('s3')

# NOTE: Define the environment variable 'model_bucket_name' in
# Lambda before running!

MODEL_GRAPH_DEF_PATH = os.path.join(os.sep, 'tmp', 'model.pb')

# Feel free to load these as environment variables through Lambda.
LABEL_STRINGS_FILENAME = os.path.join(
    'imagenet', 'imagenet_2012_challenge_label_map_proto.pbtxt')
LABEL_IDS_FILENAME = os.path.join(
    'imagenet', 'imagenet_synset_to_human_label_map.txt')

MODEL_FILENAME = 'generator.h5'

class GEN():
    def __init__(self, model_path, input_shape=(67, 120, 3)):
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

# This must be called before create_graph().
print('Downloading Model from S3...')
s3.Bucket(os.environ['model_bucket_name']).download_file(
                                                      MODEL_FILENAME,
                                                      MODEL_GRAPH_DEF_PATH)

def run_inference_on_image(image):
  """Runs inference on an image.

  Args:
    image: Image file name.

  Returns:
    Nothing
  """

  img = cv2.imread(input_path)
  shape = img.shape
  height = shape[0]
  width = shape[1]
  channel = shape[2]

  input_shape = (height, width, channel)
  gen = GEN(MODEL_PATH, input_shape)
  model = gen.generator

  pred = model.predict((img / 255)[np.newaxis, :, :, :])[0]
  out = (pred * 255).astype('u1')


  # with tf.Session() as sess:
  #   # Some useful tensors:
  #   # 'softmax:0': A tensor containing the normalized prediction across
  #   #   1000 labels.
  #   # 'pool_3:0': A tensor containing the next-to-last layer containing 2048
  #   #   float description of the image.
  #   # 'DecodeJpeg/contents:0': A tensor containing a string providing JPEG
  #   #   encoding of the image.
  #   # Runs the softmax tensor by feeding the image_data as input to the graph.
  #   softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
  #   predictions = sess.run(softmax_tensor,
  #                          {'DecodeJpeg/contents:0': image_data})
  #   predictions = np.squeeze(predictions)

  #   num_top_predictions = 5
  #   top_k = predictions.argsort()[-num_top_predictions:][::-1]
  #   results = []
  #   for node_id in top_k:
  #     human_string = NODE_LOOKUP.id_to_string(node_id)
  #     score = predictions[node_id]
  #     results.append((human_string, score))

  #   return results
  #   # print('%s (score = %.5f)' % (human_string, score))


def lambda_handler(event, context):
  results = []
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    print('Running Deep Learning example using Tensorflow library ...')
    print('Image to be processed, from: bucket [%s], object key: [%s]' % (bucket, key))

    # load image
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'wb') as f:
      s3.Bucket(bucket).download_file(key, tmp.name)
      tmp.flush()

      (prediction_label, prediction_prob) = run_inference_on_image(tmp.name)[0]

      results.append('(%s, %s)' % (str(prediction_prob), prediction_label))

  print(results)
  return results

