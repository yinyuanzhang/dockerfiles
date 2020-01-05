FROM registry.centos.org/centos:latest

RUN yum -y install java-11-openjdk-devel \
    yum -y install wget curl unzip dos2unix rpm-build rpmdevtools git openssh-clients epel-release https://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
    yum-config-manager --enable remi && \
    yum -y install vips vips-devel make gcc-c++.x86_64 && \
    yum clean all

ENV JAVA_VERSION 11
ENV JAVA_LIBDIR=/usr/share/java
ENV JNI_LIBDIR=/usr/lib/java
ENV JVM_ROOT=/usr/lib/jvm
ENV JAVA_HOME=$JVM_ROOT/java
ENV PATH=$PATH:$JAVA_HOME/bin
ENV CLASSPATH=$JAVA_HOME/lib
