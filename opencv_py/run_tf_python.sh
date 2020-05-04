#!/bin/bash

docker run --gpus all --rm -it -v $(pwd):/home/keras_opencv -p 10000:8888 keras-opencv:gpu-jupyter bash

