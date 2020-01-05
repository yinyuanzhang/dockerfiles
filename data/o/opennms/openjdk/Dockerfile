FROM centos:7

LABEL maintainer "Ronny Trommer <ronny@opennms.org>"

ARG JAVA_VERSION=1.8.0
ARG JAVA_VERSION_DETAIL=${JAVA_VERSION}.191.b12
ENV JAVA_HOME /usr/lib/jvm/java

RUN yum-config-manager --enable cr && \
    yum -y --setopt=tsflags=nodocs update && \
    yum -y install java-${JAVA_VERSION}-openjdk-devel && \
    yum -y clean all && \
    rm -rf /var/cache/yum

LABEL org.opennms.java.version="OpenJDK Devel ${JAVA_VERSION_DETAIL}"
