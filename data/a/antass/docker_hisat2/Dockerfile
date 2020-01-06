################################################################
# A Dockerfile to build hisat2 as part of RNA-seq pipeline
# Based on Ubuntu with R and tidyverse
################################################################

FROM rocker/tidyverse:3.4.2

# File Author / Maintainer
MAINTAINER Ania Tassinari <ania.tassinari@agios.com>

# install dependencies first
RUN apt-get update  && apt-get install -y \
    build-essential \
    gcc-multilib \
    zlib1g-dev \
    curl \
    wget \
    cmake \
    python \
    python-pip \
    python-dev \
    python2.7-dev \
    python-numpy \
    python-matplotlib \
    hdf5-tools \
    libhdf5-dev \
    hdf5-helpers \
    libhdf5-serial-dev \
    libssh2-1-dev \
    libcurl4-openssl-dev \
    icu-devtools \
    libssl-dev \
    libxml2-dev \
    r-bioc-biobase \
    git \
    apt-utils \
    pigz \
    default-jre


# Install Java 


# Install hisat2
WORKDIR /docker
RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-Linux_x86_64.zip && \
    unzip hisat2-2.0.5-Linux_x86_64.zip
RUN cp -p hisat2-2.0.5/hisat2 hisat2-2.0.5/hisat2-* /usr/bin

# Clean up
RUN rm -rf /docker/hisat2-2.0.5
RUN apt-get clean
RUN apt-get remove --yes --purge build-essential gcc-multilib apt-utils zlib1g-dev vim

# Set default working path
WORKDIR /docker
