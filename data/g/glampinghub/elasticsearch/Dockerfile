# Copyright (C) 2019 Glamping Hub (https://glampinghub.com)
# All rights reserved

FROM alpine

LABEL \
    version="1.2" \
    maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"

ENV MAKEFLAGS="-j$(nproc)" \
    PATH="/home/elasticsearch/elasticsearch-5.3.3/bin:${PATH}" \
    CONTAINER_ES_HOST="0.0.0.0" \
    CONTAINER_ES_PORT="9200"
WORKDIR /home/elasticsearch/elasticsearch-5.3.3/

COPY docker-entrypoint.sh /
ADD https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.3.tar.gz /tmp/

RUN apk add --no-cache openjdk8-jre su-exec bash npm gnupg py-pip \
    && adduser -D elasticsearch \
    && tar xf /tmp/elasticsearch-5.3.3.tar.gz -C /home/elasticsearch/ \
    && sed -i 's/#network.host: 192.168.0.1/network.host: ${CONTAINER_ES_HOST}\nnode.max_local_storage_nodes: 2/g' /home/elasticsearch/elasticsearch-5.3.3/config/elasticsearch.yml \
    && sed -i 's/#http.port: 9200/http.port: ${CONTAINER_ES_PORT}/g' /home/elasticsearch/elasticsearch-5.3.3/config/elasticsearch.yml \
    && npm config set unsafe-perm true \
    && npm install --production -g elasticdump@6.10.1 \
    && pip install awscli \
    && rm -rf /var/cache/apk/* /tmp/*

VOLUME ["/home/elasticsearch/elasticsearch-5.3.3/data"]
EXPOSE 9200 9300

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
