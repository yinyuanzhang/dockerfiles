# TBD? https://github.com/moby/moby/pull/31352
# ARG NODE_VERSION=latest
# FROM node:$NODE_VERSION
FROM node:latest

MAINTAINER davidkassa <david.kassa@gmail.com>

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.license="MIT" \
      org.label-schema.name="firebase-tools" \
      org.label-schema.description="Auto-updating Docker image based on NodeJS official image with Firebase Tools installed." \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/davidkassa/firebase-tools" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# Commands
RUN \
  npm install -g firebase-tools
  
