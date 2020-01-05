FROM ubuntu:16.04
MAINTAINER Chen Yuelong <yuelong.chen.btr@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ARG hipstr_version=v0.6.2

RUN apt-get update
RUN apt-get install -y gcc git zlib1g-dev libbz2-dev liblzma-dev g++ libhts-dev make
RUN cd /tmp/ && \
    git clone https://github.com/HipSTR-Tool/HipSTR.git && \
    cd HipSTR && \
    git checkout $hipstr_version && \
    make && \
    mkdir -p /opt/hipstr && \
    cp -r * /opt/hipstr

ENV PATH /opt/hipstr:$PATH


RUN apt-get clean && \
    apt-get remove --yes --purge git make && \
    rm -rf /tmp/*


CMD bash




