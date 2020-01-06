FROM ubuntu:bionic
MAINTAINER Susanna Kiwala <susanna.kiwala@wustl.edu>

LABEL \
    description="Image containing the vatools python package" \
    version="4.0.0"

RUN apt-get update -y && apt-get install -y \
    apt-utils \
    python3 \
    python3-pip \
    tcsh \
    gcc \
    build-essential \
    zlib1g-dev \
    gawk

RUN pip3 install Cython
RUN pip3 install pysam==0.9.0
RUN pip3 install vatools==4.0.0
