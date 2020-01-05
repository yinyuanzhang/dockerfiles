FROM ubuntu:latest


RUN apt-get install -f
RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

RUN apt-get update && apt-get -y upgrade \
    && apt-get update -y && apt-get install -y wget unzip \
    && wget "https://github.com/broadinstitute/picard/releases/download/2.17.2/picard.jar" \
    && mv /picard.jar /usr/bin
