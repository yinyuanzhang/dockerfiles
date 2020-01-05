FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  make \
  automake \
  pkg-config \
  git \
  g++ \
  python \
  software-properties-common

RUN apt-get update && apt-get install -y \
  libpcre3 libpcre3-dev \
  libcurl4 libcurl4-openssl-dev \
  libmysql++-dev \
  graphicsmagick-libmagick-dev-compat \
  cppcheck \
  python-pip python-dev build-essential \
  libyaml-cpp-dev \
  libcgicc-dev \
  libboost-all-dev \
  libjsoncpp-dev \
  libssl-dev

RUN apt-get update && apt-get install -y \
  rsync \
  sassc
