FROM centos:centos7

MAINTAINER heowc <heowc1992@gmail.com>

# yum update
RUN yum update -y

# install curl
RUN yum install -y curl

# install netstat, ifconfig
RUN yum install -y net-tools

# install java
ENV JDK_VERSION 8u60
ENV JDK_BUILD_VERSION b27
RUN \
	curl -LO "http://download.oracle.com/otn-pub/java/jdk/$JDK_VERSION-$JDK_BUILD_VERSION/jdk-$JDK_VERSION-linux-x64.rpm" -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
	rpm -i jdk-$JDK_VERSION-linux-x64.rpm && \
	rm -f jdk-$JDK_VERSION-linux-x64.rpm && \
	yum clean all

# setting JAVA_HOME
ENV JAVA_HOME /usr/java/default
ENV PATH $PATH:$JAVA_HOME/bin

EXPOSE 80
EXPOSE 443