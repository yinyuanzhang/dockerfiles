FROM maven:3.5-jdk-8

RUN echo 'deb http://deb.debian.org/debian sid main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get -qq -t sid install -y gettext openssh-client mysql-client

ENV GIT_SSH "/usr/bin/ssh"
