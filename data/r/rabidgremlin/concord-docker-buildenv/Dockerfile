FROM ubuntu:bionic

# Upgrade
RUN apt-get update && apt-get -y upgrade -u && apt-get clean

# Install Node and NPM
RUN apt-get -y install nodejs npm

# Install JDK
RUN apt-get -y install openjdk-8-jdk

# Install other tools
RUN apt-get -y install git

# Install library required for running embedded mysql during tests
RUN apt-get -y install libaio1 libnuma-dev
