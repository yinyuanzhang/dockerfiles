#pull from base image.
FROM node:4-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl wget git \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g gulp bower karma karma-cli webpack
