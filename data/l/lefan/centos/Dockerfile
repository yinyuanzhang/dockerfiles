# CentOS 7 + Oracle JDK 7
FROM centos:7
MAINTAINER Alexey Larin <Alexey.I.Larin@gmail.com>

ENV JDK_VERSION 7u80
ENV JDK_BUILD b15
RUN yum update -y && \
    yum install -y wget && \
    wget --no-check-certificate --no-cookies \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
         http://download.oracle.com/otn-pub/java/jdk/$JDK_VERSION-$JDK_BUILD/jdk-$JDK_VERSION-linux-x64.rpm

RUN rpm -ivh jdk-$JDK_VERSION-linux-x64.rpm && rm jdk-$JDK_VERSION-linux-x64.rpm
# Workaround for https://bugs.centos.org/view.php?id=8148
RUN chmod u+s /usr/bin/ping
