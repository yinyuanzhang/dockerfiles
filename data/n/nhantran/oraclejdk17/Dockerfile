FROM ubuntu:14.04.2
MAINTAINER Nhan Tran <tranphanquocnhan@gmail.com>
ENV REFRESHED_AT 2015-04-17

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN update-alternatives --set editor /usr/bin/vim.basic

RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jdk-7u72-linux-x64.tar.gz"
RUN tar xvf jdk-7u72-linux-x64.tar.gz && mv jdk1.7.0_72 /opt/jdk && rm jdk-7u72-linux-x64.tar.gz
RUN update-alternatives --install "/usr/bin/java" "java" /opt/jdk/bin/java 1
RUN update-alternatives --set java /opt/jdk/bin/java
ENV JAVA_HOME /opt/jdk
RUN java -version
