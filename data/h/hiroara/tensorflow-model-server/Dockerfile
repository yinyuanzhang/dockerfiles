FROM ubuntu:16.04

Maintainer Hiroki Arai <hiroara62@gmail.com>

RUN apt-get update && apt-get install -y wget software-properties-common

RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y

RUN apt-get update && apt-get install -y libstdc++6

ARG TF_VERSION=1.13.0

RUN wget "http://storage.googleapis.com/tensorflow-serving-apt/pool/tensorflow-model-server-${TF_VERSION}/t/tensorflow-model-server/tensorflow-model-server_${TF_VERSION}_all.deb" && \
    dpkg -i tensorflow-model-server_${TF_VERSION}_all.deb && \
    rm tensorflow-model-server_${TF_VERSION}_all.deb
