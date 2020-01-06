FROM jenkins/slave:alpine

USER root

RUN echo "install packages" 
RUN apk add --update \
    alpine-sdk \
    libtool \
    libltdl \
    autoconf \
    automake \
    bash \
    g++ \
    libc6-compat \
    libjpeg-turbo-dev \
    libpng-dev \
    make \
    nasm \
    nodejs \
    npm

USER root