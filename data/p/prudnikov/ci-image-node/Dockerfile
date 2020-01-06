FROM node:11
MAINTAINER Vladimir Prudnikov <v.prudnikov@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils gzip rsync && \
    rm -rf /var/cache/apk/*

