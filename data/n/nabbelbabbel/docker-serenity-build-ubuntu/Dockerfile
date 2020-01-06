FROM ubuntu:19.10

RUN apt-get update && apt-get install -y \
  wget \
  make \
  cmake \
  gcc \
  git \
  vim \
  libeigen3-dev \
  python3-pip \
  libboost-all-dev \
  libhdf5-dev \
  doxygen \
  graphviz

RUN pip3 install gcovr
