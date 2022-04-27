#! /bin/bash -xe

docker run -it --rm -p 10000:8888 \
	--user="$(id -u):$(id -g)" \
       -v "${PWD}":/home/jovyan/work \
       controlnotebook:latest 
