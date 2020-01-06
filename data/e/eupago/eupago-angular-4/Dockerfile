FROM node:9-alpine

MAINTAINER "Jeferson Kaefer" <jeferson.kaefer@eupago.pt>


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update \
        && apk upgrade \
        && apk add python \
        && apk add g++

RUN npm install angular-cli

RUN npm install --latest

EXPOSE 4200
EXPOSE 4800
