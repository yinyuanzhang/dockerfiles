FROM nginx:1.9.9

MAINTAINER alan.gibson@kapsch.net

ENV VERSION 2.0.3

RUN \
  apt-get update && \
  apt-get install -y zip unzip && \
  apt-get autoremove -y -q && \
  apt-get clean -y -q

ADD https://github.com/royrusso/elasticsearch-HQ/archive/v${VERSION}.zip /tmp/elasticsearch-HQ-${VERSION}.zip

RUN \
  unzip -q /tmp/elasticsearch-HQ-${VERSION}.zip -d /tmp && \
  mv -f /tmp/elasticsearch-HQ-${VERSION}/* /usr/share/nginx/html && \
  rm -rf /tmp/*
