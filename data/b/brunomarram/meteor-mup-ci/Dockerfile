FROM node:7.5.0
MAINTAINER Bruno Marra de Melo

RUN npm install -g mup@latest

RUN curl "https://install.meteor.com/?release=1.6.1" | sh
RUN export METEOR_ALLOW_SUPERUSER=true

RUN adduser --disabled-password --gecos '' docker_meteor
USER docker_meteor