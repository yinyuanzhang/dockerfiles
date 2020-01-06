# ------------------------------------------------------
#                       Dockerfile
# ------------------------------------------------------
# image:    node-alpine-ci
# name:     minddocdev/node-alpine-ci
# repo:     https://github.com/minddocdev/node-alpine-ci
# Requires: minddocdev/node-alpine
# authors:  development@minddoc.com
# ------------------------------------------------------
FROM minddocdev/node-alpine:latest
LABEL maintainer="development@minddoc.com"

# Install extra alpine packages
RUN apk --update add jq rsync && rm -rf /var/cache/apk/*

# Install depedencies for CI
RUN npm install --unsafe-perm -g full-icu yarn
ENV NODE_ICU_DATA="/usr/local/lib/node_modules/full-icu"
