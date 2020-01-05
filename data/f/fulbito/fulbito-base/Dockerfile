FROM ubuntu:14.04

MAINTAINER Zeta <zetahernandez@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
  
# remove several traces of debian python
RUN apt-get update && apt-get install -y \
        build-essential \
        libmysqlclient-dev \
        git \
        curl \
        wget \
        libssl-dev \
        libtiff4-dev libjpeg8-dev zlib1g-dev \
        libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev && \
        rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_us.UTF-8

ADD config/ssh_config /etc/ssh_config
ADD config/ssh/id_rsa /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/id_rsa
RUN chown -R root:root /root/.ssh
# Create known_hosts
RUN touch /root/.ssh/known_hosts
# Add bitbuckets key
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts
