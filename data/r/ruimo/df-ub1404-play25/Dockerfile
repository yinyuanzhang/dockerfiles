FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install software-properties-common wget unzip
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

RUN update-alternatives --display java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN cd /opt && \
  wget https://downloads.typesafe.com/typesafe-activator/1.3.9/typesafe-activator-1.3.9-minimal.zip && \
  unzip typesafe-activator-1.3.9-minimal.zip && \
  ln -s `pwd`/activator-1.3.9-minimal/bin/activator /usr/local/bin/

RUN cd /var && \
  mkdir dev && \
  activator new web play-scala && \
  cd web && \
  bin/activator package && \
  rm -rf /var/web

ENV SBT_OPTS "-XX:+CMSClassUnloadingEnabled -Xmx1536m"

VOLUME ["/var/home"]

EXPOSE 9000
EXPOSE 7777

CMD ["/bin/sleep", "infinity"]
