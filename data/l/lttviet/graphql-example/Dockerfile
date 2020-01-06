FROM mhart/alpine-node:6.6.0
MAINTAINER Viet Le "lttviet@gmail.com"

ENV NODE_ENV production

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
ADD . .

RUN apk add --no-cache bash \
  && npm i --production \
  && npm i pm2 -g

EXPOSE 4000

ENTRYPOINT pm2 start --no-daemon build/index.js
