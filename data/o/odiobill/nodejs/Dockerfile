# Debian based container for running nodejs scripts
# VERSION               0.1
FROM debian:jessie
MAINTAINER Davide Lucchesi  "davide@lucchesi.nl"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y nodejs npm
RUN apt-get clean

VOLUME /srv
WORKDIR /srv

CMD /bin/bash

