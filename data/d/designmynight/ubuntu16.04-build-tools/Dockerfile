FROM ubuntu:16.04

RUN apt-get update && \
      apt-get -y install \
      build-essential \
      git \
      wget \
      curl \
      unzip \
      ca-certificates \
      libffi-dev \
      libreadline6-dev \
      libssl-dev \
      libyaml-dev \
      ssh \
      ruby-dev \
      zlib1g-dev && \
      apt-get -y clean autoclean autoremove && \
      rm -rf /var/lib/{apt,dpkg,cache,log}/