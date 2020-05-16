#!/bin/bash

# set up opencv-python in tf-docker
# Because of area selection while install, it's exexuted after docker build
# user shall be added

usermod -u $USER_ID -o -m user
groupmod -g $GROUP_ID user

# opencv-devのインストール
apt-get update -y
apt-get install -y libopencv-dev
apt-get clean
rm -rf /var/lib/apt/lists/*

# adduser $USER

# Opencvのインストール
pip install opencv-python
