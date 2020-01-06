FROM openjdk:8u111-jdk-alpine
LABEL maintainer "kevin.wittek@groovy-coder.com"

RUN apk add --update \
               libstdc++ \
               bash && \
    rm /var/cache/apk/*

ENTRYPOINT /bin/bash