FROM bitnami/minideb:stretch
MAINTAINER eskabetxe

ARG JAVA_VERSION=openjdk-8-jdk
ENV version=${JAVA_VERSION}

RUN install_packages apt-utils ${version}

ENV PATH /usr/bin/java:$PATH

RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)" /docker-java-home
ENV JAVA_HOME /docker-java-home

ENV LANG C.UTF-8
ENV TZ Europe/Madrid

RUN echo done
