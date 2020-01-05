FROM ubuntu:14.04
MAINTAINER app@purpleworks.co.kr

ENV DEBIAN_FRONTEND noninteractive 

# update ubuntu latest
RUN \
  apt-get -qq update && \
  apt-get -qq -y dist-upgrade

# install essential packages
RUN \
  apt-get -qq -y install build-essential software-properties-common python-software-properties git curl


# Install MongoDB
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*

# Define mountable directories
VOLUME ["/data/db"]
VOLUME ["/data/configdb"]

# Expose ports
EXPOSE 27017
EXPOSE 27018
EXPOSE 27019

# Entrypoint
CMD ["usr/bin/mongod"]
