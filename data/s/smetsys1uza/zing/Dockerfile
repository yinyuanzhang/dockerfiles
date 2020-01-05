FROM ubuntu:18.04

RUN apt-get -qq update && \
    apt-get install -yqq gnupg2 locales && \
    locale-gen en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 0xB1998361219BD9C9 && \
    echo "deb http://repos.azul.com/zing/ubuntu bionic main" >> /etc/apt/sources.list.d/zing.list && \
    apt-get -qq update && \
    apt-get install -y zing-jdk11.0.0=19.07.0.0-4 && \
    rm -rf /var/lib/apt/lists/*
