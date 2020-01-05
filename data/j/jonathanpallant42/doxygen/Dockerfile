# Basic Doxygen container - based on Ubuntu 18.04
# Includes graphviz, mscgen and curl
#
# Copyright (c) 42 Technology Ltd
# This file is licensed under the MIT license

FROM ubuntu:18.04
LABEL com.42technology.doxygen.version="1.0.0"
LABEL com.42technology.doxygen.date="2019-03-26"
MAINTAINER Jonathan Pallant (jonathan.pallant@42technology.com)
RUN apt-get update && apt-get -y install doxygen mscgen curl graphviz && rm -rf /var/lib/apt/lists/*
RUN mkdir /work
WORKDIR /work
CMD [ "doxygen" ]
