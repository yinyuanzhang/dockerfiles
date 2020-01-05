FROM ubuntu:16.04
MAINTAINER Serfim TIC

# Base MVN / NPM
RUN apt update && apt install -y \
  locales \
  build-essential \
  git \
  openjdk-8-jdk \
  maven \
  curl 
  
# Install Python/ Pip
RUN apt install -y python-pip

# Install AWS CLI
RUN pip install awscli --ignore-installed six
