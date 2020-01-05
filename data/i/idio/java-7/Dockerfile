FROM ubuntu:14.04
MAINTAINER David Przybilla <david.przybilla@idioplatform.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:chris-lea/redis-server
RUN add-apt-repository ppa:webupd8team/java
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y --force-yes oracle-java7-installer sbt maven
