FROM node:10.13-alpine as node-angular
LABEL authors="Daniel Díaz"

#Linux setup
RUN apk update \
  && apk add --update alpine-sdk \
  && apk del alpine-sdk \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache verify \
  && sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd

RUN npm set progress=false
RUN npm install -g npm@latest
RUN npm install -g rimraf
RUN npm install -g @angular/cli@latest
