# Dockerfile for Oracle JDK 7 in Ubuntu

FROM ubuntu:14.04

MAINTAINER Sandu Cecan <scecan@gmail.com>

RUN apt-get update && apt-get install -y wget && \
wget -P /tmp/java --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jdk-8u11-linux-x64.tar.gz && \
mkdir /opt/jdk && \
tar -zxf /tmp/java/jdk-8u11-linux-x64.tar.gz -C /opt/jdk && \
rm -rf /tmp/java

ENV JAVA_HOME /opt/jdk/jdk1.8.0_11

ENV PATH $PATH:$JAVA_HOME/bin
