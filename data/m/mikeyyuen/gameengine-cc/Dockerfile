FROM ubuntu:18.04

MAINTAINER Michael Yuen <michael.yuen@mac.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -yqq && apt-get install -yqq \
      ca-certificates \
      clang-7 \
      clang-format-7 \
      curl \
      gcc \
      git-core \
      libssl-dev \
      libc++-dev \
      libz-dev \
      make \
      python \
      time \
      unzip \
      valgrind \
  && rm -rf /var/lib/apt/lists/*

ENV DOCKER_VER="17.05.0-ce"

RUN curl -fsSL -o /tmp/docker-${DOCKER_VER}.tgz https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VER}.tgz && \
    tar --strip-components=1 -xvzf /tmp/docker-${DOCKER_VER}.tgz -C /usr/local/bin && \
    rm /tmp/docker-${DOCKER_VER}.tgz

RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-7 100 && \
    update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-7 100 && \
    ln -s /usr/bin/clang-7 /usr/bin/clang && \
    ln -s /usr/bin/clang++-7 /usr/bin/clang++ && \
    ln -s /usr/bin/clang-format-7 /usr/bin/clang-format

RUN mkdir -p /gameengine && \
    mkdir -p /gameengine/bin && \
    mkdir -p /gameengine/data && \
    mkdir -p /gameengine/build

ENV PATH "$PATH:/gameengine/bin"

WORKDIR /gameengine/build


