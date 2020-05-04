#!/bin/bash

# docker run --rm -it -v $PWD:/work tf_opencv bash
docker run -v $(pwd):/tf/works -p 10000:8888 keras:vgg16_opencv


