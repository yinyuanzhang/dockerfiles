FROM node:12.10.0-alpine

RUN apk add --no-cache bash git openssh

RUN mkdir /home/node/app

COPY package.json /home/node/app

WORKDIR /home/node/app

RUN npm install -G
