FROM golang:1.11-alpine

ENV CONCOURSE_VERSION 4.2.2
ENV JQ_VERSION 1.5

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    git

# Install jq
RUN wget https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64 && \
    chmod +x jq-linux64 && \
    mv jq-linux64 /usr/bin/jq

# Install fly
RUN wget https://github.com/concourse/concourse/releases/download/v${CONCOURSE_VERSION}/fly_linux_amd64 && \
    chmod +x fly_linux_amd64 && \
    mv fly_linux_amd64 /usr/bin/fly

# Install stopover
RUN go get github.com/EngineerBetter/stopover