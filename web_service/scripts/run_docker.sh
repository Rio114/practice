#!/bin/bash

docker run --rm -it -u $USER -v $PWD:/home/web -p 8000:8000 mysite:latest bash
