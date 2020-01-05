FROM phusion/baseimage:latest
MAINTAINER Koert Zeilstra <koert.zeilstra@zencode.nl>

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y --no-install-recommends oracle-java8-installer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

CMD ["/sbin/my_init"]
    
