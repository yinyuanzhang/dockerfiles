FROM alpine

MAINTAINER sahsu.mobi@gmail.com

RUN apk add --update nodejs nodejs-npm && \
      rm /var/cache/apk/*
RUN npm install -g jsonlint && npm install -g jsondiffpatch && npm install -g prettyjson && npm install -g json-minify && npm install -g html-validator-cli && npm install -g cli-stopwatch && npm install -g yaml-lint && npm install -g node-readability
