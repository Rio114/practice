#!/bin/bash

cd ~/../usr/local
mkdir nvidia
cd nvidia
mkdir include
mkdir lib64

cd ~/../home/keras_opencv
cp -a cuda/include/cudnn.h /usr/local/nvidia/include/
cp -a cuda/lib64/libcudnn* /usr/local/nvidia/lib64/
chmod a+r /usr/local/nvidia/include/cudnn.h /usr/local/nvidia/lib64/libcudnn*
