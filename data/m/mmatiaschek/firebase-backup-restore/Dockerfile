#LABEL maintainer="mmatiaschek@gmail.com"

#FROM alpine:3.8
#RUN apk add npm git
#RUN npm install firestore-backup-restore
#ADD package.json

FROM ubuntu:18.04
RUN apt-get update && apt-get install -y git npm
RUN npm install -g firestore-backup-restore

ENTRYPOINT [ "firestore-backup-restore" ]