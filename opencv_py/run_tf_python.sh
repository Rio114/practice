#!/bin/bash

# docker run --rm -it -v $PWD:/work tf_opencv bash
docker run --rm -v $(pwd):/tf/works -p 10000:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter

