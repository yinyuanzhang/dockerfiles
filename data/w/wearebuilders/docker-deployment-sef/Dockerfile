#checkout: https://github.com/dotsunited/docker-git-ftp
FROM ubuntu:16.04
MAINTAINER We.Are.Builders

ENV DOCKER_FILE_VERSION=0.0.4

# build show info script
COPY show_info.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/show_info.sh

# build show info script
COPY sef-deploy.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/sef-deploy.sh

# install git and other deps
RUN apt-get -qq update
RUN apt-get -qq install git wget libssl-dev build-essential software-properties-common

# add the newest git-ftp PPA and update the installation
RUN add-apt-repository ppa:git-ftp/ppa
RUN apt-get update
RUN apt-get install -qy git-ftp

# get and build libssh2 and curl
RUN wget https://www.libssh2.org/download/libssh2-1.8.0.tar.gz
RUN tar -xvzf libssh2-1.8.0.tar.gz
RUN cd libssh2-1.8.0 && ./configure && make && make install
RUN wget https://curl.haxx.se/download/curl-7.54.0.tar.bz2
RUN tar -xvjf curl-7.54.0.tar.bz2
RUN cd curl-7.54.0 && ./configure --with-libssh2=/usr/local && make && make install
RUN ldconfig
