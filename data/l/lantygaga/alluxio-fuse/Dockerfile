#
# ModelArts Fuse Base
#

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y ppa:openjdk-r/ppa && \
	apt-get update && \
	apt-get install -y --no-install-recommends \
	openjdk-8-jdk openjdk-8-jre-headless libfuse-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

