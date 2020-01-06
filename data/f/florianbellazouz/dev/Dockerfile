FROM node:8-alpine

WORKDIR /root

RUN apk add curl jq sed libc6-compat git
RUN npm i node-dev -g

CMD node-dev index.js
