FROM node:10.15-jessie AS build

RUN apt-get autoclean
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -u -y dist-upgrade
RUN apt-get install -y\
    autoconf \
    automake \
    bash \
    g++ \
    libpng-dev \
    make \
    nasm \
    libgl1-mesa-dev \
    libxi6

RUN npm install --global gatsby-cli
