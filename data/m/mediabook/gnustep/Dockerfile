# Base Image, Nvidia CUDA
FROM nvidia/cuda:9.0-devel

MAINTAINER Scott Christley <schristley@mac.com>

# Install OS Dependencies
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
#RUN dpkg --add-architecture i386  # Enable 32-bit repos for libx11-dev:i386
RUN DEBIAN_FRONTEND='noninteractive' apt-get update
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y \
    build-essential git subversion ninja cmake libffi-dev libxml2-dev libxslt1-dev \
    libgnutls-dev libicu-dev libblocksruntime-dev libkqueue-dev libpthread-workqueue-dev autoconf libtool \
    libjpeg-dev libtiff-dev libffi-dev libcairo-dev libxt-dev curl wget emacs gobjc \
    libdispatch-dev

# install gnustep
RUN mkdir /mediabook
RUN mkdir /mediabook/gnustep-src

RUN cd /mediabook/gnustep-src && wget https://github.com/gnustep/tools-make/archive/make-2_7_0.tar.gz
RUN cd /mediabook/gnustep-src && tar xf make-2_7_0.tar.gz
RUN cd /mediabook/gnustep-src/tools-make-make-2_7_0 && ./configure && make install

RUN cd /mediabook/gnustep-src && wget https://github.com/gnustep/libs-base/archive/base-1_25_1.tar.gz
RUN cd /mediabook/gnustep-src && tar xf base-1_25_1.tar.gz
RUN cd /mediabook/gnustep-src/libs-base-base-1_25_1 && ./configure && make && make install

# GNUstep build environment
RUN /sbin/ldconfig
ENV GNUSTEP_MAKEFILES /usr/local/share/GNUstep/Makefiles

# TACC mount points
RUN mkdir /corral-tacc
RUN mkdir /corral-repl
RUN mkdir /gpfs
RUN mkdir /scratch
RUN mkdir /work
RUN mkdir /home1
