FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y openjdk-8-jdk wget

RUN mkdir /rundeck
WORKDIR /rundeck
RUN wget -q https://dl.bintray.com/rundeck/rundeck-maven/rundeck-3.1.0-20190731.war && \
  java -Dserver.web.context=/rundeck -jar rundeck-3.1.0-20190731.war --installonly

COPY rundeck-config.properties server/config/rundeck-config.properties
EXPOSE 4440/tcp
CMD ["java", "-Dserver.web.context=/rundeck", "-jar", "rundeck-3.1.0-20190731.war"]
