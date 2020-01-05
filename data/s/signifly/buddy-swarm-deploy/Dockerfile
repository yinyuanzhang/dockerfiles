FROM alpine:3.9

RUN apk update && apk add openssh-client

RUN mkdir -p ~/.ssh
RUN chmod 700 ~/.ssh

COPY ./deploy.sh /usr/bin/deploy
