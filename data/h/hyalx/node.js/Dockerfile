FROM alpine:edge
MAINTAINER Indexyz <r18@iinde.xyz>

RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories\
    && apk update && apk upgrade \
    && apk add --no-cache nodejs-lts@edge 
