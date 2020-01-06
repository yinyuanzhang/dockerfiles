FROM golang:1.11-alpine

RUN apk add --no-cache build-base fuse git openssh-sftp-server

RUN adduser -h /home/build -s /bin/ash -G users -D build

USER build
