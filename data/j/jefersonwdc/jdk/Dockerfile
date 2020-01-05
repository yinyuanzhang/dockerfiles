FROM ubuntu:18.04

LABEL maintainer="jeferson.wc@outlook.com"

RUN apt-get update -y && \
    apt-get install openjdk-8-jdk -y

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH ${JAVA_HOME}/bin:$PATH