FROM ubuntu:18.04

MAINTAINER jmonlong@ucsc.edu

RUN apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        wget \
        curl \
        python3 \
        python3-pip \
        python3-setuptools \
        python3-dev \
        gcc \
        less \
        nano \
        make \
        libncurses5-dev libncursesw5-dev \
        zlib1g-dev libbz2-dev liblzma-dev \
        libcurl4-openssl-dev libssl-dev \
        && rm -rf /var/lib/apt/lists/*


WORKDIR /samtools

COPY . /samtools

RUN ./configure && make && make install

WORKDIR /home
