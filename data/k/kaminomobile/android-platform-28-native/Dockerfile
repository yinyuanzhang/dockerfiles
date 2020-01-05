# ====================================================================== #
# Android Native Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM kaminomobile/android-platform-28:112

# Author
# ---------------------------------------------------------------------- #
LABEL blazsolar "blaz@kamino.si"

USER root

# Instal make
RUN apt-get update && apt-get install -y build-essential \
    sudo \
    libboost-all-dev \
    libprotobuf-dev \
    protobuf-compiler \
    clang-3.6 \
    clang-format-3.6 \
    ninja-build \
    wget \
    git \
    make \
    libcurl4-openssl-dev \
    zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install cmake
RUN cd /usr/local/src \ 
    && wget https://cmake.org/files/v3.15/cmake-3.15.2.tar.gz \
    && tar xvf cmake-3.15.2.tar.gz \ 
    && cd cmake-3.15.2 \
    && ./bootstrap --system-curl \
    && make \
    && make install \
    && cd .. \
    && rm -rf cmake*

USER jenkins

