FROM schmich/armv7hf-alpine-qemu
# This FROM worked to build on DockerHub but caused this error on OrangePi Zero Armbian 
# docker run -it gounthar/alpine-linux-curl /bin/bash
# standard_init_linux.go:190: exec user process caused "exec format error"
#FROM resin/qemux86-alpine:latest

RUN ["cross-build-start"]
MAINTAINER Gounthar Frankfurt <116569+gounthar@users.noreply.github.com>

USER root

RUN apk update && apk upgrade && apk add curl\
  && rm -fr /tmp/*
  
RUN ["cross-build-end"]
