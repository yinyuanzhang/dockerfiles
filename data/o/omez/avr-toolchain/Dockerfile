FROM ubuntu:latest
MAINTAINER Alexander Sergeychik <alexander@sergeychik.com>

RUN apt-get update && apt-get install -y apt-utils

RUN apt-get update && apt-get install -y locales && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN apt-get update && apt-get install -y \
    gcc-avr \
    avr-libc \
    avrdude

#RUN rm -rf /var/lib/apt/lists/*

VOLUME /app
WORKDIR /app

