FROM debian:jessie

RUN apt-get update && apt-get install -y wget

RUN mkdir /opt/jdk &&\
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /opt/jdk/jdk.tar.gz http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.tar.gz &&\
    tar xpfo /opt/jdk/jdk.tar.gz -C /opt/jdk --strip 1 &&\
    rm /opt/jdk/jdk.tar.gz

ENV JAVA_HOME /opt/jdk
ENV PATH $PATH:/opt/jdk/bin
