FROM node:10.6.0-alpine

LABEL name="nodevana"
LABEL description="A NodeJs Alpine image with bash and git as the only packages"

ENV BUILD_PACKAGES bash build-base git

RUN apk update && \
    apk upgrade && \
    apk add $BUILD_PACKAGES && \
    rm -rf /var/cache/apk/*
