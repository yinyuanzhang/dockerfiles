FROM debian:jessie
MAINTAINER Carl Janzen <carl.janzen@gmail.com>

RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >> /etc/apt/sources.list \
  && apt-get update -q \
  && apt-get install -qy \
    ffmpeg \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /data
VOLUME ["/data"]
