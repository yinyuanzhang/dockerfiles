FROM node:8.9-slim

LABEL "Author"="Andrew Kemp <hello@ankemp.com>"
LABEL "Version"="1.0"

ARG USER_HOME_DIR="/tmp"
ARG APP_DIR="/app"
ARG USER_ID=1000

ENV NPM_CONFIG_LOGLEVEL warn

USER root

# Install packages not included in slim
RUN apt-get update && \
  apt-get install --assume-yes sudo apt-transport-https

# Configure Debian Package Repository & install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install yarn

WORKDIR $APP_DIR