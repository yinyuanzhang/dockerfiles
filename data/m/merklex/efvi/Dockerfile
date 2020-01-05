FROM ubuntu:18.04

RUN apt-get update && \
  apt-get install -y wget build-essential cmake autoconf automake

RUN wget https://www.openonload.org/download/openonload-201805.tgz && \
  mkdir /build && mv openonload-201805.tgz /build && \
  cd /build && \
  tar -xvf openonload-201805.tgz && \
  cd /build/openonload-201805/scripts && \
  ./onload_build --user && \
  cd /build/openonload-201805/build/gnu_x86_64 && \
  cp lib/ciul/libciul1.a /usr/local/lib/ && \
  cp lib/citools/libcitools1.a /usr/local/lib && \
  cd /build/openonload-201805/src/include && \
  cp -r ci /usr/local/include/ && \
  cp -r etherfabric /usr/local/include/ && \
  cd / && \
  rm -rf /build

RUN apt-get remove -y wget build-essential cmake autoconf automake && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*
