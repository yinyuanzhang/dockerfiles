FROM obcon/baseimage

MAINTAINER http://obcon.de Marco Obermeyer <marco.obermeyer@obcon.de>

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

RUN apt-get update 

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections

RUN apt-get install -y ca-certificates-java
RUN apt-get install -y oracle-java8-set-default

RUN rm -rf /var/lib/apt/lists/*
