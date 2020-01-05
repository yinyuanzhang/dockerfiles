# jungrafael/alpine-ssh

FROM alpine

RUN mkdir -p ~/.ssh \
 && chmod 700 ~/.ssh \
 && touch ~/.ssh/id_rsa \
 && chmod 600 ~/.ssh/id_rsa

RUN apk update && apk add --no-cache openssh-client bash
