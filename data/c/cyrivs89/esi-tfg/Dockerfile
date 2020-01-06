FROM debian:latest

MAINTAINER Cyrivs89 <1.marioromero1989@gmail.com>

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    build-essential \
    locales \
    locales-all
ENV LC_ALL es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES.UTF-8
RUN wget -qO- http://pike.esi.uclm.es/add-pike-repo.sh | sh
RUN apt-get install -y \
    esi-tfg
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*
