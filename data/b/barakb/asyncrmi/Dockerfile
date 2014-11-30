FROM ubuntu

#Replace dash with bash

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

MAINTAINER Barak Bar Orion <barak.bar@gmail.com>

# Install Java.

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get install -y oracle-java8-installer ca-certificates


ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


RUN apt-get -y install wget

RUN wget --no-verbose -O /tmp/apache-maven-3.0.5.tar.gz \
    http://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz

# stop building if md5sum does not match
RUN echo "94c51f0dd139b4b8549204d0605a5859  /tmp/apache-maven-3.0.5.tar.gz" | \
    md5sum -c

# install in /opt/maven
RUN mkdir -p /opt/maven

RUN tar xzf /tmp/apache-maven-3.0.5.tar.gz --strip-components=1 \
    -C /opt/maven

RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.0.5.tar.gz


RUN sudo apt-get -y install git


RUN git clone https://github.com/barakb/asyncrmi.git /data/asyncrmi
WORKDIR /data/asyncrmi


RUN mvn install

# RUN apt-get install -y vim


CMD ["bash"]

