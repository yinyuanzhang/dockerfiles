# Docker image based on phusion with Oracle JDK8
FROM phusion/baseimage:0.9.22
MAINTAINER Enrico Maria Carmona, e.carmona@asst-monza.it

# Fix locale issue, see https://github.com/phusion/baseimage-docker/issues/276
RUN locale-gen it_IT.UTF-8
ENV LANG=it_IT.UTF-8 \
    LANGUAGE=it:en \
    LC_ALL=it_IT.UTF-8 \
# Set correct JAVA environment variable
    JAVA_HOME=/usr/lib/jvm/java-8-oracle

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# https://github.com/phusion/baseimage-docker#upgrading_os
RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confold"

# java8
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get -qq update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -f -y -q \
    oracle-java8-installer

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
