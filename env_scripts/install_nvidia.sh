#!/bin/bash

# run with 'sudo'

apt install build-essential

wget http://us.download.nvidia.com/XFree86/Linux-x86_64/430.64/NVIDIA-Linux-x86_64-430.64.run
chmod 755 NVIDIA-Linux-x86_64-430.64.run
./NVIDIA-Linux-x86_64-430.64.run

wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run
chmod 755 cuda_10.1.243_418.87.00_linux.run
./cuda_10.1.243_418.87.00_linux.run
