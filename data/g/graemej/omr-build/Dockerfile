FROM ubuntu:trusty

MAINTAINER Graeme Johnson <graeme@johnson-family.ca>

RUN apt-get update 

# Install basic development dependencies (ruby is required to build OMR)
RUN env DEBIAN_FRONTEND=noninteractive \
 apt-get install -y --no-install-recommends \
 libtcmalloc-minimal4 \
 libssl-dev \
 build-essential \
 g++-multilib \
 git \
 libreadline-dev \
 nano \
 ruby \
 silversearcher-ag

# Install OMR dependencies
RUN env DEBIAN_FRONTEND=noninteractive \
 apt-get install -y --no-install-recommends \
 autoconf \
 bison \
 libnuma-dev

# Script to run the build steps
ADD build_it / 