FROM mhart/alpine-node:10 

LABEL authors="Saber Karmous"

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

#Angular CLI
RUN npm install -g @angular/cli

