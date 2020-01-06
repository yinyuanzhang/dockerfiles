# JAVA 7
#
# VERSION 0.0.1
#

FROM debian:wheezy

MAINTAINER Samuel Nasello <samuel.nasello@elosi.com>

RUN apt-get update && \
	apt-get install -y curl tar \
	&& (curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u60-b19/jdk-7u60-linux-x64.tar.gz | tar xfz -) \
	&& mv /jdk1.7.0_60/jre /jre1.7.0_60 \
    && mv /jdk1.7.0_60/lib/tools.jar /jre1.7.0_60/lib/ext \
    && rm -Rf /jdk1.7.0_60\
	&& ln -s /jre1.7.0_60 /java
	
# Set JAVA_HOME
ENV JAVA_HOME /java
ENV PATH $PATH:$JAVA_HOME/bin