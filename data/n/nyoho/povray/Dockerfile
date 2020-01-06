# POV-Ray

FROM ubuntu:12.04

RUN \
  date && apt-get update && apt-get -y install \
  build-essential git zlib1g-dev libpng-dev libjpeg-dev libtiff-dev libboost-thread-dev autoconf

RUN \
  mkdir /src && \
  cd /src && \
  git clone https://github.com/POV-Ray/povray.git && \
  cd povray/unix && \
  ./prebuild.sh && \
  cd .. && \
  ./configure COMPILED_BY="your name <email@address>" && \
  make && \
  make install && \
  date

WORKDIR /src
