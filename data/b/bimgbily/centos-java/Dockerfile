FROM centos:latest

RUN yum -y update \  
      && yum install wget -y \
      && yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel -y \
      && yum clean all

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el8_0.x86_64