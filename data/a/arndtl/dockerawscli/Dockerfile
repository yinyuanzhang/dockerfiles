FROM docker:latest

MAINTAINER Lothar Arndt <lothar.arndt@equality-it.com.au>

RUN apk --no-cache add \
      bash \
      curl \
      jq \
      python \
      py-pip && \
      pip install awscli && \
      mkdir /root/.aws
