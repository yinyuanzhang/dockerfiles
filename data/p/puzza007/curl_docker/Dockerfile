FROM ubuntu:18.04

MAINTAINER Paul Oliver

RUN apt-get -qq update \
    && apt-get -qq -y install \
               autoconf \
               gcc \
               git \
               libevent-dev \
               libssl-dev \
               libtool \
               make \
               curl \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/curl/curl.git \
    && cd curl \
    && ./buildconf \
    && ./configure --with-ssl --with-zlib \
    && make install \
    && cd .. \
    && rm -rf curl
