FROM node:slim

RUN apt-get update && apt-get install -y software-properties-common apt-transport-https apt-utils

#Wine
RUN apt-get install software-properties-common \
    && dpkg --add-architecture i386  \
    && apt-add-repository 'https://dl.winehq.org/wine-builds/debian' \
    && wget http://dl.winehq.org/wine-builds/Release.key && apt-key add Release.key

#Install protobuf build pipeline for golang
RUN apt-get update && apt-get install -y winehq-stable \
