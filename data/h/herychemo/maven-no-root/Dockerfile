FROM maven:latest
MAINTAINER Heriberto Reyes Esparza <hery.chemo@gmail.com>

RUN useradd -m -d /var/maven maven -s /bin/bash

ARG USER_HOME_DIR="/var/maven"

ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

USER maven
WORKDIR $USER_HOME_DIR

