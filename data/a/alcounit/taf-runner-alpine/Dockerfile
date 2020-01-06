FROM maven:3.6-jdk-8-alpine

MAINTAINER Danylo Kuvshynov <alcounit@gmail.com>

ARG GROOVY_VERSION=2.5.2

RUN apk -U upgrade && \
    apk add libstdc++ curl ca-certificates bash wget git xvfb alsa-lib freetype giflib libgcc libjpeg-turbo libpng libx11 libxrender libxtst musl libxext libxi xz

RUN wget https://dl.bintray.com/groovy/maven/apache-groovy-binary-${GROOVY_VERSION}.zip \
    -O /tmp/groovy.zip && \
    unzip /tmp/groovy.zip -d /usr/local && \
    ln -s /usr/local/groovy-${GROOVY_VERSION} /usr/local/groovy && \
    ln -s /usr/local/groovy/bin/groovy /usr/local/bin/groovy

RUN apk del curl wget && \
    rm -rf /tmp/*

USER root