FROM node:10-alpine

# install dependencies
RUN apk -U --no-cache add bash openjdk8

RUN npm i npm -g
RUN npm i firebase-tools -g

RUN firebase setup:emulators:firestore
