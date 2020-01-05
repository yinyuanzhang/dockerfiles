FROM node:10.13-alpine

LABEL mantainer="Devsbetstarters <devs@betstarters.com>"

RUN apk --update --no-cache \
    add jq rsync openssh-client bash git perl curl openssh-client

RUN npm install -g ajv@^6.9.1
RUN npm install -g @angular/compiler-cli@8.0.0
RUN npm install -g @angular/cli@8.0.2

