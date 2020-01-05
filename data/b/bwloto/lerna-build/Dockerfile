FROM node:10-alpine

RUN apk update && apk upgrade
RUN apk add --update python python-dev py-pip build-base bash
RUN pip install awscli --upgrade --user && apk --purge -v del py-pip && rm -rf /var/cache/apk/*
RUN yarn global add lerna