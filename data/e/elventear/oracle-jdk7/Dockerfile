# use the ubuntu base image provided by dotCloud
FROM debian:jessie

MAINTAINER Pepe Barbe <dev@antropoide.net>

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list.d/oracle-jdk.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list.d/oracle-jdk.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get update 

# accept Oracle license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | \
    /usr/bin/debconf-set-selections && apt-get -y install oracle-java7-installer
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle
