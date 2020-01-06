FROM jenkins/jenkins:2.121.2-alpine

MAINTAINER ghahaman007@gmail.com

ENV MAVEN_VER="3.5.3" \
 MAVEN_HOME="/usr/lib/mvn" \
 PATH=$PATH:/usr/lib/mvn/bin  

USER root

RUN apk add --no-cache --update curl \
	&& rm -rf /var/cache/apk/*  \	
	&& curl -fsSL http://archive.apache.org/dist/maven/maven-3/${MAVEN_VER}/binaries/apache-maven-${MAVEN_VER}-bin.tar.gz -o apache-maven-${MAVEN_VER}-bin.tar.gz \
    && tar -zxvf apache-maven-${MAVEN_VER}-bin.tar.gz \
    && mv apache-maven-${MAVEN_VER} ${MAVEN_HOME} \
	&& rm apache-maven-${MAVEN_VER}-bin.tar.gz 

USER jenkins