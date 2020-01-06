FROM node:10.9.0-alpine

RUN cd ~ && npm install npm@6.0.0 && rm -rf /usr/local/lib/node_modules && mv node_modules /usr/local/lib/

RUN apk update && apk upgrade \
  && apk add --no-cache bash git openssh rsync \
  && npm install -g grunt-cli
