FROM phusion/baseimage:0.9.16

MAINTAINER Ralf Anton Beier version: 0.1

ENV DEBIAN_FRONTEND noninteractive
CMD ["/sbin/my_init"]


RUN apt-get update && apt-get install -y bash software-properties-common && add-apt-repository ppa:george-edison55/cmake-3.x && apt-get update && apt-get install -y cmake libicu-dev git python build-essential

RUN chmod 755 /etc/container_environment
RUN chmod 755 /etc/container_environment/*
RUN chmod 644 /etc/container_environment.sh /etc/container_environment.json

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -ms /bin/bash developer
USER developer
WORKDIR /home/developer

RUN mkdir git && cd git && git clone https://github.com/meta-toolkit/meta.git && cd meta/ && git reset --hard v1.3.2 && git submodule update --init --recursive && mkdir build && cd build && cp ../config.toml . && cmake ../ -DCMAKE_BUILD_TYPE=release && make -j 20

