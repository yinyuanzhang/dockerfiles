# Base Image - Node Platform
FROM node:alpine
LABEL maintainer="jules@umpisa.co" version="0.0.1"

# Install Firebase CLI
RUN yarn global add firebase-tools
RUN echo "ipv6" >> /etc/modules
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
  echo "http://dl-3.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
  echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories; \
  echo "http://dl-5.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk update
RUN apk add --no-cache \
    libtool \
    autoconf \
    automake \
    bash \
    g++ \
    libc6-compat \
    libjpeg-turbo-dev \
    libpng-dev \
    make \
    nasm \
    build-base
