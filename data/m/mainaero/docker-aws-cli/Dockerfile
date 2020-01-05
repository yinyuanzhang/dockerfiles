FROM alpine:3.8

WORKDIR /app

RUN apk update && \
   apk add aws-cli --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted --no-cache
RUN apk add --no-cache make dateutils openssh-client rsync
