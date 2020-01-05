FROM node:latest

MAINTAINER nazayasu

RUN mkdir /hubot
ADD . /hubot
WORKDIR /hubot

CMD ["bin/hubot", "--adapter", "slack"]
