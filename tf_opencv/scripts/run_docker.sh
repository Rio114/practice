#!/bin/bash

# for setup
# docker run --gpus all -it --name gpu_temp -v $(pwd):/home/gpu -p 8888:8888 gpu:temp bash

# to make image
# docker commit gpu_temp gpu:opencv

# after setup
# docker run --gpus all -it -u $(id -u):$(id -g) --name gpu -v $(pwd):/home/gpu -p 8888:8888 gpu:opencv bash

# for network
# docker network create srgan-service
# docker run --gpus all --network srgan-service -it -u $(id -u):$(id -g) --name gpu -v $(pwd):/home/gpu -p 8888:8888 gpu:opencv bash

# for use
docker start -i gpu
