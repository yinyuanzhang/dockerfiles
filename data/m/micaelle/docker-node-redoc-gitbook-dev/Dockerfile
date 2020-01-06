FROM node:lts-alpine
MAINTAINER Michael Fedchenko <michael.fedchenko@gmail.com>

RUN apk add -q curl zip
RUN npm --silent -g install redoc-cli gitbook-cli
RUN gitbook fetch 3.2.3
RUN gitbook install --log warn
