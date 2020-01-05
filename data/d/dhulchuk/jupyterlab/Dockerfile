FROM ubuntu:18.04

LABEL maintainer="Danyla Hulchuk <danyla.hulchuk@gmail.com>"

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Update the apt-get and installs utils
RUN apt-get update \
  && apt-get install -y curl gnupg2 software-properties-common

# Add repo for python3.7
RUN add-apt-repository -y ppa:deadsnakes/ppa

# Update node version on apt-get
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

# Run simulated install to check latest package versions in repository
#RUN apt-cache policy \
#   python3.7 \
#   python3.7-dev \
#   python3-pip \
#   python3-setuptools \
#   nodejs \
#   build-essential \
#   libzmq3-dev

# Installs node.js, python, pip and setup tools
RUN apt-get install -y \
    python3.7=3.7.4-1+bionic2 \
    python3.7-dev=3.7.4-1+bionic2 \
    python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
    python3-setuptools=39.0.1-2 \
    nodejs=10.16.0-1nodesource1 \
    build-essential=12.4ubuntu1 \
    libzmq3-dev=4.2.5-1ubuntu0.2

# Set default python3 to python3.7
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 10

#RUN python3 --version

# Setup python language
ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8

# Upgrade pip
RUN pip3 install --upgrade pip

# Upgrade npm
RUN npm install npm@latest -g

# Install jupyter notebook
RUN pip3 install \
  jupyter==1.0.0 \
  jupyterlab==1.0.2 \
  nbresuse==0.3.2

# Fix ipython kernel version
RUN ipython3 kernel install

# Install nodejs kernel
RUN npm config set user 0 \
 && npm config set unsafe-perm true \
 && npm install ijavascript -g

RUN ijsinstall --hide-undefined --install=global
