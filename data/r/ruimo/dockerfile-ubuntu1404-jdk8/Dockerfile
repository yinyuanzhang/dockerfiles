FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update

# automatically accept oracle license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
# and install java 8 oracle jdk
RUN apt-get -y install oracle-java8-installer && apt-get clean
RUN update-alternatives --display java
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
