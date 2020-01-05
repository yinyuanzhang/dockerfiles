FROM debian:jessie

RUN apt-get update && apt-get install -y wget

RUN mkdir /opt/jre &&\
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /opt/jre/jre.tar.gz http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jre-8u91-linux-x64.tar.gz &&\
    tar xpfo /opt/jre/jre.tar.gz -C /opt/jre --strip 1 &&\
    rm /opt/jre/jre.tar.gz

ENV JAVA_HOME /opt/jre
ENV PATH $PATH:/opt/jre/bin
