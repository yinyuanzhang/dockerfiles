FROM debian:8.5
MAINTAINER Dmitry Petrov <dmitry@fullstackml.com>

LABEL com.fullstackml = "true" \
      com.fullstackml.function = "base-docker-images/debian-java" \
      com.fullstackml.version = "1.0"

# Install java. See http://www.webupd8.org/2014/03/how-to-install-oracle-java-8-in-debian.html
RUN apt-get update --fix-missing && \
    apt-get install -y wget && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer oracle-java8-set-default && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/cache/oracle* /var/log/* && \
    rm -rf /usr/lib/jvm/java-8-oracle/man /usr/lib/jvm/java-8-oracle/src.zip /usr/lib/jvm/java-8-oracle/javafx-src.zip /tmp/*
