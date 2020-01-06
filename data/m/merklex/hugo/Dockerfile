FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN mkdir /work

RUN cd /work && \
    wget https://github.com/gohugoio/hugo/releases/download/v0.50/hugo_extended_0.50_Linux-64bit.tar.gz && \
    tar -xvf hugo_extended_0.50_Linux-64bit.tar.gz && \
    mv hugo /
