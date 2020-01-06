#
# Docker build file for Vynosny project
#
FROM ubuntu:14.10
MAINTAINER Bob Rosum <rerosum@gmail.com>

RUN lsb_release -a

RUN sudo apt-get install -y software-properties-common

# Install Java 8
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer && \
  java -version

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

VOLUME /data

CMD ["java", "-jar", "/var/lib/jenkins/jobs/Vynosny/workspace/target/scala-2.11/vynosny-assembly-1.0.jar"]
