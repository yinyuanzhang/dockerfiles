FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install openjdk-7-jdk

RUN update-alternatives --display java
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

ADD profile /profile

CMD ["/bin/bash", "--rcfile", "/profile", "-i"]
