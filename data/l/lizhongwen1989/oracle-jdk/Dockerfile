FROM ubuntu:16.04

MAINTAINER github.com/Official-Registry, lizhongwen1989@gmail.com

RUN apt-get update -y \
  && apt-get install -y curl tar \
  && cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ENV JAVA_VERSION=1.7.0_80
ENV JAVA_HOME=/opt/java/jdk${JAVA_VERSION}
ENV PATH=${PATH}:${JAVA_HOME}/bin

RUN curl --fail --location --retry 3 --header "Cookie: oraclelicense=accept-securebackup-cookie; " \
  http://download.oracle.com/otn-pub/java/jdk/7u80-b15/jdk-7u80-linux-x64.tar.gz \
  -o /tmp/jdk-7u80-linux-x64.tar.gz \
  && mkdir -p /opt/java \
  && tar -zvxf /tmp/jdk-7u80-linux-x64.tar.gz -C /opt/java/ \
  && rm -rf /tmp/jdk-7u80-linux-x64.tar.gz ${JAVA_HOME}/src.zip ${JAVA_HOME}/javafx-src.zip
