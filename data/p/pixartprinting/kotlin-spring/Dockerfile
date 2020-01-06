FROM maven:3.5-jdk-8-alpine

USER root

COPY ./code/ /home
WORKDIR /home

RUN mvn clean install
