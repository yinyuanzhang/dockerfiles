FROM ubuntu:16.04
MAINTAINER Serfim TIC

# Base
RUN apt update && apt install -y \
  locales \
  build-essential \
  git \
  openjdk-8-jdk \
  maven \
  curl \
  wget \
  unzip
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt install -y nodejs
  
