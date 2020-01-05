FROM ubuntu:18.04

MAINTAINER Ayush Shanker <shankerayush@gmail.com>

RUN echo 'deb-src http://security.ubuntu.com/ubuntu/ bionic universe main' >> /etc/apt/sources.list

RUN apt update && \
    apt install -y \
    git build-essential curl

RUN apt install -y \
    libexpat1-dev libmpdec-dev zlib1g-dev libffi-dev \
    libssl-dev libsqlite3-dev libncurses5-dev

RUN git clone --depth 1 https://github.com/python/cpython

RUN cd cpython && \
    git submodule update --init && \
    ./configure --prefix=/opt/py38 --enable-shared \
     --with-system-expat --with-system-ffi \
     --with-system-libmpdec --enable-optimizations \
     --enable-loadable-sqlite-extensions && \
    make -j4 && \
    make install

RUN tar cJvf py38.txz /opt/py38

RUN curl --upload-file ./py38.txz https://transfer.sh/py38.txz
