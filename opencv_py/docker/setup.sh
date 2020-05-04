#!/bin/bash
# opencv-devのインストール
apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# TensorflowとOpencvのインストール
pip3 install opencv-python
