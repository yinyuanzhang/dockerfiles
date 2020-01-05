FROM ubuntu:16.04

MAINTAINER WuXi NextCODE DevOps <devops@wuxinextcode.com>

RUN apt-get dist-upgrade -y --no-install-recommends && \
	apt-get update && \
	apt-get -y install --no-install-recommends apt-transport-https ca-certificates && \
	apt-get -y install --no-install-recommends language-pack-en && \
	locale-gen en_US && \
	update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 && \
	apt-get -y install --no-install-recommends software-properties-common && \
	add-apt-repository ppa:webupd8team/java -y && \
	echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
	apt-get update && \
	apt-get install -y --no-install-recommends oracle-java8-installer && \
	apt-get install -y --no-install-recommends oracle-java8-set-default && \
	rm -rf /var/cache/oracle-jdk8-installer && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# set default java environment variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/
ENV TZ=UTC
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

