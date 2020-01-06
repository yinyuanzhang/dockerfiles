FROM debian:stable-slim
MAINTAINER https://bitbucket.org/bluesquall/docker-movesense/issues

RUN apt-get update && apt-get install -y \
  build-essential \
  cmake \
  curl \
  gcc-arm-none-eabi \
  ninja-build \
  python \
  python-pip \
  && apt-get clean

RUN pip install nrfutil

