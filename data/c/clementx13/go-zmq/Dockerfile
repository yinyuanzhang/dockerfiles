FROM golang:1.12-stretch

ENV LIBZMQ_VERSION v4.3.1

WORKDIR /

USER root

RUN apt-get update && apt-get install -y \
    autoconf \
    build-essential \
    libtool \
    automake \
    pkg-config\
    unzip \
    libkrb5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b ${LIBZMQ_VERSION} --depth 1 https://github.com/zeromq/libzmq.git \
    && cd /libzmq \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && ldconfig \
    && cd / \
    && rm -rf libzmq

RUN groupadd -g 1000 appuser \
    && useradd -rm -d /home/appuser  -u 1000 -g appuser appuser
USER appuser
WORKDIR /home/appuser
RUN go get -u github.com/pebbe/zmq4
