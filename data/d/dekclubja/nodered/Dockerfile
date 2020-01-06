FROM nodered/node-red-docker:slim

USER root

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

USER node-red

RUN npm install node-red-contrib-mongodb3
RUN npm install node-red-contrib-mssql

COPY settings.js /data
