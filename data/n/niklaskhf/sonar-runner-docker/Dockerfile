FROM alpine:latest

MAINTAINER Niklas Kammhoff <niklas@kammhoff.com>


# install git / java / curl 
RUN apk add --no-cache openjdk8 curl git unzip sed bash

# set env vars
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

WORKDIR /root

RUN curl --insecure -o ./sonarscanner.zip -L https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip
RUN unzip sonarscanner.zip
RUN rm sonarscanner.zip

# add sonar-runner to path
ENV SONAR_RUNNER_HOME=/root/sonar-scanner-3.2.0.1227-linux 
ENV PATH $PATH:/root/sonar-scanner-3.2.0.1227-linux/bin 


# use openjdk8 instead of embedded jre 
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' /root/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner