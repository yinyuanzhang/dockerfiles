FROM node:lts-stretch
MAINTAINER Rodrigue Villetard <rodrigue.villetard@gmail.com>

RUN wget --quiet https://github.com/elm/compiler/releases/download/0.19.1/binary-for-linux-64-bit.gz \
    && gunzip binary-for-linux-64-bit \
    && chmod +x binary-for-linux-64-bit \
    && mv binary-for-linux-64-bit /usr/local/bin/elm \
    && elm 

RUN npm install --global  --unsafe-perm=true --allow-root \
    create-elm-app \
    elm-format \
    elm-live \
    elm-test \
    elm-upgrade

ENV LANG en_US.UTF-8
ENV TERM xterm-256color

WORKDIR /app
