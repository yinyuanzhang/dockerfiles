FROM ubuntu:xenial

MAINTAINER Rafaat Hossain <rafaat123@gmail.com>

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV DEBIAN_FRONTEND noninteractive
ENV TERM ${TERM:-dumb}

RUN apt-get update && \
    apt-get -y --allow-unauthenticated \
            install unzip wget git curl rpm maven \
            ant ivy nodejs npm ruby rubygems libdbd-mysql-perl \
            tomcat7 openjdk-8-jdk mysql-server && \
    apt-get clean

CMD /bin/bash
