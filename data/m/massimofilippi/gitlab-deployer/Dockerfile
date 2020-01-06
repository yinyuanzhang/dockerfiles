FROM node:8

LABEL maintainer="Massimo Filippi"

# Install stuff
RUN    apt-get update  \
    && apt-get -y upgrade \
    && curl -sL https://sentry.io/get-cli/ | bash \
    && npm install -g firebase-tools \
    && npm install -g lighthouse
