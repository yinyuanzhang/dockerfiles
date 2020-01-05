FROM ubuntu:18.04

MAINTAINER path-help@sanger.ac.uk

ARG DEBIAN_FRONTEND=noninteractive

ARG BUILD_DIR=/tmp/local-install

# Ubuntu
RUN apt-get update -qq -y && \
    apt-get upgrade -qq -y && \
    apt-get clean

# Dependencies for singularity and python
RUN apt-get update -qq -y && \
    apt-get install -qq -y \
      wget \
      libcurl4-gnutls-dev \
      build-essential \
      zlib1g-dev \
      libncurses5-dev \
      libbz2-dev \
      liblzma-dev \
      python3-pip \
      python3.7-dev \
      libpython3.7-dev && \
    apt-get clean

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

# Samtools 0.1.19
RUN cd /opt && \
    wget -q https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download -O samtools-0.1.19.tar.bz2 && \
    tar xf samtools-0.1.19.tar.bz2 && \
    rm samtools-0.1.19.tar.bz2 && \
    chmod 755 samtools-0.1.19 && \
    cd samtools-0.1.19 && \
    make
ENV PATH /opt/samtools-0.1.19:$PATH

# featureCounts (subread)
RUN cd /opt && \
    wget -q https://sourceforge.net/projects/subread/files/subread-1.4.5-p1/subread-1.4.5-p1-Linux-x86_64.tar.gz/download -O subread-1.4.5-p1-Linux-x86_64.tar.gz && \
    tar xf subread-1.4.5-p1-Linux-x86_64.tar.gz && \
    rm subread-1.4.5-p1-Linux-x86_64.tar.gz
ENV PATH /opt/subread-1.4.5-p1-Linux-x86_64/bin:$PATH

# Tabix 0.2.5
# We have to sed the makefile to get this old version to compile
RUN cd /opt && \
    wget -q https://downloads.sourceforge.net/project/samtools/tabix/tabix-0.2.5.tar.bz2 && \
    tar xf tabix-0.2.5.tar.bz2 && \
    cd tabix-0.2.5 && \
    sed -ir 's/-lz -L. -ltabix/-L. -ltabix -lz/g' Makefile && \
    make
ENV PATH /opt/tabix-0.2.5:$PATH

# Baker
COPY . "${BUILD_DIR}"
RUN cd "${BUILD_DIR}" && \
   python3 setup.py test && \
   pip3 install . && \
   cd regression_tests && \
   ./run.sh && \
   rm -rf "${BUILD_DIR}"
