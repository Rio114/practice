#!/bin/bash

# docker run --gpus all -it -u $(id -u):$(id -g) --name keras-cv -v $(pwd):/home/work -p 8888:8888 keras-cv:latest

# for network
# docker network create srgan-service
# docker run --gpus all --network srgan-service -it -u $(id -u):$(id -g) --name gpu -v $(pwd):/home/gpu -p 8888:8888 gpu:opencv bash

# for use
docker start -i keras-cv
