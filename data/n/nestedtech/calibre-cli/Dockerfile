FROM node:9-alpine

RUN npm install calibre -g

RUN apk --update upgrade && \
  apk add --no-cache jq && \
  find / -type f -iname \*.apk-new -delete && \
  rm -rf /var/cache/apk/*

