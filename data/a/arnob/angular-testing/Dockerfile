# Contatiner have been developed for testing of node packages
# This container runs node
FROM node:latest
MAINTAINER You

# Installing google browser from (https://www.google.com/linuxrepositories/)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  google-chrome-stable \
  npm nodejs nodejs-legacy \
  build-essential chrpath libssl-dev libxft-dev \
  libfreetype6 libfreetype6-dev \
  libfontconfig1 libfontconfig1-dev \
  libexif12 \
  default-jre \
  imagemagick \
  xvfb git && \
  apt-get autoremove -y --purge \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN npm install --global npm@latest

RUN npm install -g inherits \
  && npm install -g \
  yo \
  bower \
  yarn \
  grunt-cli \
  jasmine-node \
  eslint \
  eslint-plugin-angular \
  eslint-config-angular \
  jasmine-reporters@1.0.0 \
  karma \
  karma-chrome-launcher \
  karma-firefox-launcher \
  karma-jasmine \
  karma-junit-reporter \
  karma-ng-scenario \
  && rm -rf /root/.npm/

RUN google-chrome --version

ENV NODE_PATH /usr/lib/nodejs/:/usr/local/lib/node_modules/
ENV CHROME_BIN /usr/bin/google-chrome