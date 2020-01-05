FROM ubuntu:14.10

MAINTAINER Larry Liang

# Install prerequisites
RUN apt-get update
RUN apt-get install -y software-properties-common

#Install java8
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y --force-yes oracle-java8-installer
