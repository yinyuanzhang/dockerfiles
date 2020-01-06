FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install --no-install-recommends build-essential software-properties-common -y \
  && add-apt-repository ppa:george-edison55/cmake-3.x -y \
  && add-apt-repository ppa:ubuntu-toolchain-r/test -y \
  && apt-get update \
  && apt-get install --no-install-recommends cmake gcc-6 g++-6 -y \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6 \
  && apt-get clean \
  && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
