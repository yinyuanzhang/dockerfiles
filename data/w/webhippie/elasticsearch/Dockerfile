FROM webhippie/alpine:latest

LABEL maintainer="Thomas Boerger <thomas@webhippie.de>" \
  org.label-schema.name="Elasticsearch" \
  org.label-schema.vendor="Thomas Boerger" \
  org.label-schema.schema-version="1.0"

VOLUME ["/var/lib/elasticsearch"]

ENTRYPOINT ["/usr/bin/entrypoint"]
CMD ["/usr/bin/server"]
EXPOSE 9200 9300
WORKDIR /var/lib/elasticsearch

ENV ELASTICSEARCH_VERSION 6.4.0
ENV ELASTICSEARCH_TARBALL https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz

RUN apk update && \
  apk upgrade && \
  mkdir -p \
    /var/lib/elasticsearch && \
  groupadd \
    -g 1000 \
    elastico && \
  useradd \
    -u 1000 \
    -d /var/lib/elasticsearch \
    -g elastico \
    -s /bin/bash \
    -M \
    elastico && \
  apk add \
    coreutils \
    java-jna-native \
    openjdk8-jre && \
  rm -rf \
    /var/cache/apk/*

RUN mkdir -p \
    /usr/share/elasticsearch && \
  curl -sLo - \
    ${ELASTICSEARCH_TARBALL} | tar xvzf - --strip 1 --exclude config --exclude logs --exclude plugins --exclude LICENSE.txt --exclude NOTICE.txt --exclude README.textile --exclude bin/*.bat --exclude bin/*.exe --exclude modules/x-pack-ml -C /usr/share/elasticsearch && \
  ln -sf \
    /usr/share/elasticsearch/bin/elasticsearch* \
    /usr/bin/ && \
  ln -sf \
    /usr/share/elasticsearch/bin/xpack* \
    /usr/bin/ && \
  ln -sf \
    /var/lib/elasticsearch/plugins \
    /usr/share/elasticsearch/plugins && \
  chown elastico:elastico \
    /usr/share/elasticsearch

ADD rootfs /
