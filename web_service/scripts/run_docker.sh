#!/bin/bash

# docker run --name web -it -u $(id -u):$(id -g) -v $PWD:/home/web -p 8000:8000 web:django bash

docker start -i web