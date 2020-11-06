#!/bin/bash

# docker run --gpus all -it -u $(id -u):$(id -g) --name keras-cv -v $(pwd):/home/work -p 8888:8888 keras-cv:latest

# for network
# docker network create gan-serv
# docker run --gpus all --network gan-serv -it -u $(id -u):$(id -g) --name gan-serv -v $(pwd):/home/work -p 8888:8888 keras-cv:latest

# for use
docker start -i keras-cv
