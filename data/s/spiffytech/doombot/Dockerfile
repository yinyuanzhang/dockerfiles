FROM node:13-alpine

RUN mkdir /app
COPY package.json package-lock.json /app/
WORKDIR /app
RUN npm install
COPY .  /app/

CMD bin/hubot -a discord
