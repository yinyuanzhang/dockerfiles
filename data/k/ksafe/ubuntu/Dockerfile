FROM ubuntu:14.04
MAINTAINER ksafe <ksafer@gmail.com>

#将APT源替换成Aliyun的
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get update
#将系统组件升级到最新
RUN apt-get -y upgrade
#安装常用软件(vim wget git)
RUN apt-get -y install vim wget git python

#安装Oracle Java 7
RUN apt-get -y install software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
#自动确认授权
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java7-installer && apt-get clean
RUN update-alternatives --display java 
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment
