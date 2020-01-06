# Based on: https://registry.hub.docker.com/u/webratio/java/

FROM hedlund/ubuntu
MAINTAINER henrik@hedlund.im

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common && \
	DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:webupd8team/java -y && \
	DEBIAN_FRONTEND=noninteractive apt-get update -y && \
	echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java6-installer && \
	DEBIAN_FRONTEND=noninteractive apt-get remove software-properties-common -y && \
	DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
	DEBIAN_FRONTEND=noninteractive apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-6-oracle