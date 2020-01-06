FROM node:lts-alpine as angular-cli

LABEL authors="Sebastian Wegert"

RUN apk update \
  && apk add --update alpine-sdk \
  && npm install -g @angular/cli@8.3.6 \
  && apk del alpine-sdk \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache verify \
  && sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd
