#!/bin/bash

# set up opencv-python in tf-docker
# Because of area selection, exexuted after docker build

# opencv-devのインストール
apt-get update -y
apt-get install -y libopencv-dev
apt-get clean
rm -rf /var/lib/apt/lists/*

# TensorflowとOpencvのインストール
pip install opencv-python
