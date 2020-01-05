# JAVA 8
#
# VERSION 0.0.1
#

FROM debian:wheezy

MAINTAINER Samuel Nasello <samuel.nasello@elosi.com>

RUN apt-get update && \
	apt-get install -y curl tar \
	&& (curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u20-b26/jdk-8u20-linux-x64.tar.gz | tar xfz -) \
	&& mv /jdk1.8.0_20/jre /jre1.8.0_20 \
    && mv /jdk1.8.0_20/lib/tools.jar /jre1.8.0_20/lib/ext \
    && rm -Rf /jdk1.8.0_20 \
	&& ln -s /jre1.8.0_20 /java
	
# Set JAVA_HOME
ENV JAVA_HOME /java
ENV PATH $PATH:$JAVA_HOME/bin