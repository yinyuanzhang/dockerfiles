FROM ubuntu:14.04

MAINTAINER Adam Zielinski <adam@maosmurf.com>

# ubuntu docker image already contains "force-unsafe-io"

# prevent services from restarting
# see http://jpetazzo.github.io/2013/10/06/policy-rc-d-do-not-start-services-automatically/
# already contained in ubuntu:14.04
# RUN echo $'#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d
# RUN chmod +x /usr/sbin/policy-rc.d

RUN apt-get -qq update
RUN apt-get -qqy upgrade

# install oracle jdk6
RUN apt-get -qqy install software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get -qq update
RUN echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -qqy install oracle-java6-installer

# clean
RUN apt-get clean
RUN apt-get autoremove -yq
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV JAVA_HOME /usr/lib/jvm/java-6-oracle

ENV HOME /root
