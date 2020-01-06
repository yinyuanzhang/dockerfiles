FROM debian:jessie

MAINTAINER Albert Alvarez Bruned <albert@albertbruned>

ENV DEBIAN_FRONTEND noninteractive
ENV DISPLAY :0.0

RUN dpkg --add-architecture i386 && \
    apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
        wget xz-utils libc6:i386 libdbus-1-3 libasound2 libsm6 libxfixes3 \
        libdbus-1-3:i386 libasound2:i386 libexpat1:i386 libfontconfig1:i386 \
        libfreetype6:i386 libjpeg62:i386 libpng12-0:i386 libsm6:i386 \
        libxdamage1:i386 libxext6:i386 libxfixes3:i386 libxinerama1:i386 \
        libxrandr2:i386 libxrender1:i386 libxtst6:i386 zlib1g:i386


