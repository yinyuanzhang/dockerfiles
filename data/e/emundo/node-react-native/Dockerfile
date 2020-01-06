FROM node:9.8.0-alpine

## dependencies
RUN apk update && apk upgrade
RUN apk add git
RUN apk add build-base
RUN apk add python
RUN apk add ncurses

## emundo user
RUN addgroup -g 9999 aws && \
    # We need this group for AWS
    adduser -h /home/emundo -D -s /bin/bash -G aws emundo 

USER emundo
WORKDIR /home/emundo

## Enable global node packages without the need of sudo.
## This simplifies the installation of tools like reason-cli.
RUN npm config set prefix $HOME/npm
ENV PATH="/home/emundo/npm/bin:${PATH}"

## This can be used to install os-specific packages like reason-cli.
ENV OS="linux"
