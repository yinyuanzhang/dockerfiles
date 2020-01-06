FROM node:10-stretch
MAINTAINER "Thiago Pereira Rosa <thiagor [at] engineer.com>"

RUN apt-get update && DEBIAN_FRONTEND="noninteractive"
RUN apt-get install -y --no-install-recommends chromium libgconf-2-4 openjdk-8-jre-headless
RUN npm install -g gulp
RUN rm -rf /var/lib/apt/lists/*

USER node

ENV CHROME_BIN /usr/bin/chromium
