FROM ubuntu:16.04
MAINTAINER Serfim TIC

RUN apt update && apt install -y \
  locales \
  build-essential \
  gcc-4.8 \
  g++-4.8 \
  git \
  openjdk-8-jdk \
  curl \
  wget \
  python \
  unzip \
  ffmpeg

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt install -y nodejs
