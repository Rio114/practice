#!/bin/bash

docker run --gpus all -it -v $(pwd):/home/keras_opencv -p 10000:8888 tf2-opencv:gpu bash

