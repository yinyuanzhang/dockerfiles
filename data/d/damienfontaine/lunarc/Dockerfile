FROM golang:1.10-stretch
MAINTAINER Damien Fontaine <damien.fontaine@lineolia.net>

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -

RUN apt-get update && apt-get install -y \
  npm \
  nodejs \
  libfreetype6 \
  libfontconfig
