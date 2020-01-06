FROM ubuntu:latest
MAINTAINER Ivan <ivan@marsud.id>

RUN apt-get update && apt-get install -y software-properties-common

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN echo Node 6.1.0 && \
    apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install -y nodejs build-essential git && apt-get autoclean

WORKDIR /app
