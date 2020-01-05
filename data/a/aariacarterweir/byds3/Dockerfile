# Extend the latest ubuntu image
FROM alpine:latest

# Set a working directory
WORKDIR /source/

# Add package.json to prep node package cache
COPY package.json .

# Update / Upgrade apk
RUN apk update

# Install apk packages
RUN apk add \
    nodejs \
    yarn

# RUN YARN TO ADD PACKAGES FROM PACKAGE.JSON
RUN yarn install

# ADD NODE_MODULES/.bin to $PATH
ENV PATH="/source/node_modules/.bin/:${PATH}"

# CLEAN UP
RUN rm -rf /source/*
RUN rm /var/cache/apk/*

# Set entrypoint to "sh"
ENTRYPOINT ["sh"]
