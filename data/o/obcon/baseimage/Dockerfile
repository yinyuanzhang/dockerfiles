FROM phusion/baseimage:0.9.16

MAINTAINER http://obcon.de Marco Obermeyer <marco.obermeyer@obcon.de>

RUN sed -e 's/^# deb /deb /g' /etc/apt/sources.list | grep "^deb " > /etc/apt/sources.list.new && mv /etc/apt/sources.list.new /etc/apt/sources.list

RUN cat /etc/apt/sources.list 

RUN apt-get update 

RUN apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    wget \
    git \
    openssh-client \
    subversion  \
    unzip

RUN rm -rf /var/lib/apt/lists/*