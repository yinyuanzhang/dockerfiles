FROM docker:latest
MAINTAINER Heriberto Reyes Esparza <hery.chemo@gmail.com>

RUN apk update

RUN apk fetch openjdk8
RUN apk add openjdk8

RUN apk fetch maven
RUN apk add maven

ENV PATH="/usr/lib/jvm/java-1.8-openjdk/bin:${PATH}"

