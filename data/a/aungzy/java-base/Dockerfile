# Java base container using OpenJDK to run a java app under /app directory.
FROM openjdk:latest

MAINTAINER Aung Zay Yar Lwin <aungzayyar@gmail.com>

VOLUME /tmp

ENV APPDIR /app

WORKDIR $APPDIR

ENV JAVA_OPTS ""

# Entrypoint to run java file (Based on Spring Boot Docker documentation - https://spring.io/guides/gs/spring-boot-docker/)
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar `find $APPDIR -name *.jar`" ]
