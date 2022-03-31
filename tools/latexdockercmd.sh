#!/bin/sh
#Script must be run from the source code's directory
IMAGE=blang/latex:ubuntu
if [ $# -eq 0 ]
  then
   thingstorun=bash 
fi

docker run --rm -it --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data \
--user $(id -u):$(id -g) \
 "$IMAGE" "$thingstorun" 
