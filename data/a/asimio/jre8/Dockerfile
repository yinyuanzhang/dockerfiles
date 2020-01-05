# Ubuntu 14.04. Used to build a base image with latest JRE 8.
# Build image with: sudo docker build -t asimio:jre8 .

FROM ubuntu:14.04
MAINTAINER Orlando L Otero <ootero@asimio.net>, https://bitbucket.org/asimio/java.git

# Update Ubuntu
RUN \
  bash -c 'apt-get -qq update && apt-get -y upgrade && apt-get -y autoclean && apt-get -y autoremove' && \
  bash -c 'DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget tar'

# Install JRE
RUN \
  mkdir -p /usr/lib && \
  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u74-b02/server-jre-8u74-linux-x64.tar.gz && \
  tar -zxf server-jre-8u74-linux-x64.tar.gz -C /usr/lib && \
  mv /usr/lib/jdk1.8.0_74 /usr/lib/jre && \
  chown -R root:root /usr/lib/jre

# Env variables
ENV \
  JAVA_HOME /usr/lib/jre && \
  PATH $JAVA_HOME/bin:$PATH

CMD ["bash"]
