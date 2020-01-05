#
# Base image consisting of Debian, Java 7, Ant, Maven and Git
#
FROM java:7

MAINTAINER Tako Schotanus <tako@ceylon-lang.org>

LABEL org.ceylon-lang.dockerfile.description="Base image consisting of Debian, Java 7, Ant, Maven and Git" \
    org.ceylon-lang.dockerfile.vendor="RedHat" \
    org.ceylon-lang.dockerfile.version="1.1"

RUN apt-get -y update && \
    apt-get install -y git ant maven docbook2x sudo patch && \
    apt-get clean

