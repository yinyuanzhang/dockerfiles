# Ubuntu 14.04 + JDK 8 base image 
# Build image locally with: sudo docker build -t asimio:jdk8 .

FROM ubuntu:14.04
MAINTAINER Orlando L Otero <ootero@asimio.net>, https://bitbucket.org/asimio/java.git

# Update Ubuntu
RUN \
  bash -c 'apt-get -qq update && apt-get -y upgrade && apt-get -y autoclean && apt-get -y autoremove' && \
  bash -c 'DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget tar'

# Install JDK
RUN \
  mkdir -p /usr/lib && \
  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u74-b02/jdk-8u74-linux-x64.tar.gz && \
  tar -zxf jdk-8u74-linux-x64.tar.gz -C /usr/lib && \
  mv /usr/lib/jdk1.8.0_74 /usr/lib/jdk && \
  chown -R root:root /usr/lib/jdk

# Env variables
ENV \
  JAVA_HOME /usr/lib/jdk && \
  PATH $JAVA_HOME/bin:$PATH

CMD ["bash"]