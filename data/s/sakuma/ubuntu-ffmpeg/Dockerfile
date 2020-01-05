FROM ubuntu:trusty
MAINTAINER nao.bear@gmail.com

RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository 'deb http://ppa.launchpad.net/jon-severinsson/ffmpeg/ubuntu '"$(cat /etc/*-release | grep "DISTRIB_CODENAME=" | cut -d "=" -f2)"' main'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1DB8ADC1CFCA9579
RUN apt-get update
RUN apt-get install -y ffmpeg
