FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y dist-upgrade

RUN apt-get install -y composer rsync openssh-client php-mbstring php-curl unzip php-mailparse npm
RUN npm -g install tcs sass
