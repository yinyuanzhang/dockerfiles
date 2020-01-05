FROM ubuntu:18.04

MAINTAINER simojenki

RUN apt-get update && \
    apt-get install -y \
        locales \
        maven \
        openjdk-11-jdk-headless

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /airsonic

WORKDIR /airsonic

RUN mvn test package

FROM linuxserver/airsonic:latest
COPY --from=0 /airsonic/airsonic-main/target/airsonic.war /app/airsonic/airsonic.war

