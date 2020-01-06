FROM node:8-alpine

# Define Versions
ENV NPM_VERSION 6.4.1

# install dependencies build dependencies
RUN apk add --update --no-cache \
  python \
  python-dev \
  make  \
  expat \
  musl \
  python2 \
  g++ \
  && apk upgrade --no-cache


#Create  app folder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install defined NPM version and app dependencies which we cant pack with webpack
RUN npm -g install npm@$NPM_VERSION && \
  rm -rf node_modules &&  \
  npm install level pouchdb express-pouchdb --build-from-source --production --silent