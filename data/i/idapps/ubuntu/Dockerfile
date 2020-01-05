FROM ubuntu:14.04

MAINTAINER Javier Fonseca <idapps.ve@gmail.com>

# Install dependencies
RUN sudo apt-get update && sudo apt-get install -y curl autoconf pkg-config g++ libssl-dev openssl libffi-dev tar ca-certificates software-properties-common wget build-essential git-core nano python-dev python3-pip git gcc bcrypt

# Install Python 3.5
RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz; tar xzvf Python-3.5.2.tgz; cd Python-3.5.2; ./configure; make; sudo make install
RUN alias python=python3
