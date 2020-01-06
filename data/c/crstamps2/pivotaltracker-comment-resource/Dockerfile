FROM ruby:alpine

RUN apk update \
 && apk add jq \
 && rm -rf /var/cache/apk/*
# COPY assets
COPY check /opt/resource/check
COPY in /opt/resource/in
COPY out /opt/resource/out

RUN chmod +x /opt/resource/check /opt/resource/out /opt/resource/in

WORKDIR /opt/resource