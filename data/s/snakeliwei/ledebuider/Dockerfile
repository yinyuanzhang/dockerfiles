FROM ubuntu:18.04
LABEL maintainer="lyndon <snakeliwei@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get update && \
    apt-get -y install wget curl \
                       build-essential \
                       asciidoc \
                       binutils \
                       bzip2 \
                       gawk \
                       gettext \
                       git \
                       libncurses5-dev \
                       libz-dev \
                       patch \
                       unzip \
                       zlib1g-dev \
                       lib32gcc1 \
                       libc6-dev-i386 \
                       subversion \
                       flex \
                       uglifyjs \
                       git-core \
                       gcc-multilib \
                       p7zip \
                       p7zip-full \
                       msmtp \
                       libssl-dev \
                       texinfo \
                       libglib2.0-dev \
                       xmlto \
                       qemu-utils \
                       autoconf \
                       automake \
                       libtool \
                       autopoint && \
    mkdir -p /src/lede && \
    git clone https://github.com/coolsnowwolf/lede /src/lede && \
    cd /src/lede && \ 
    ./scripts/feeds update -a && \
    ./scripts/feeds install -a
