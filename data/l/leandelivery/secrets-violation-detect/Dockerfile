FROM golang:alpine as gobuild

# METADATA
LABEL maintainer="team@lean-delivery.com"

# build cred-alert
RUN apk --no-cache add unzip
RUN apk add --no-cache --virtual .build-dependancies git \
    && go get github.com/pivotal-cf/cred-alert \
    && go install github.com/pivotal-cf/cred-alert

# install detect-secrets
FROM python:3.6.0-alpine

RUN apk --no-cache add unzip git
RUN	pip install detect-secrets

COPY --from=gobuild /go/bin/cred-alert /usr/bin
