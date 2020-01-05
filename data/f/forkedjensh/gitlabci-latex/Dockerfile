FROM ubuntu
MAINTAINER Jens Heidbüchel <forkedjensh+dockerhub@mailbox.org>

ENV REFRESHED_AT 2018-12-22
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yqq update
RUN apt-get -yqq install git curl openssh-client fonts-liberation2 texlive-full plantuml graphviz
RUN apt-get -yqq clean
