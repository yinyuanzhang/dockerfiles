FROM openjdk:8-jdk
MAINTAINER Guilhem Eydieux

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y maven
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g gulp
