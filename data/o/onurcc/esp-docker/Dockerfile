FROM debian:buster

#
# Build ESP
#

## Dependencies for building ESP
RUN apt-get update && \
  apt-get install -y \
    automake \
    autotools-dev \
    bash \
    build-essential \
    curl \
    g++ \
    git \
    gnupg \
    libtool \
    m4 \
    openjdk-11-jdk-headless \
    openjdk-11-source \
    pkg-config \
    python \
    unzip \
    uuid-dev \
    wget \
    zip \
    zlib1g-dev

## Checkout ESP
RUN mkdir /src

WORKDIR /src

RUN git clone https://github.com/cloudendpoints/esp && \
  cd esp && \
  git submodule update --init --recursive

## Install Bazel
RUN cd esp && \
  bash -c "source script/tools/linux-install-bazel && update_bazel"

## Build ESP Binary
RUN cd esp && \
  bazel build //src/nginx/main:nginx-esp

## Install ESP
RUN cp esp/bazel-bin/src/nginx/main/nginx-esp /usr/local/bin/nginx-esp && \
  mkdir /usr/local/etc/nginx-esp && \
  cp esp/src/nginx/conf/* /usr/local/etc/nginx-esp

## Remove bazel and clean up
RUN rm -rf /root/.cache && \
  rm -rf /usr/local/lib/bazel && \
  rm /usr/local/bin/bazel && \
  rm -rf /src/esp
