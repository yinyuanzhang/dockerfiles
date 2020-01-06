FROM ubuntu:18.04

ENV UBUNTU_VERSION=18.04
ENV GCC_VERSION=7-2018q2

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
  && apt install -y build-essential cmake software-properties-common \
  && add-apt-repository ppa:team-gcc-arm-embedded/ppa -y \
  && apt update \
  && apt install -y gcc-arm-embedded=${GCC_VERSION}-*

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
