FROM node:8-alpine

RUN apk update
RUN apk upgrade
RUN apk add rsync
RUN apk add openssh


WORKDIR /localDebugRepo

VOLUME ["/localDebugRepo"]

ENTRYPOINT ["/bin/sh"]