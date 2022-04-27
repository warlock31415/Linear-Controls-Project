#!/bin/sh
#Script must be run from the source code's directory
IMAGE=blang/latex:ubuntu
if [ $# -eq 0 ]
  then
   thingstorun=bash 
else
   thingstorun= bash -c "$@"
fi


docker run --rm -it --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data \
 "$IMAGE" "$thingstorun" 
