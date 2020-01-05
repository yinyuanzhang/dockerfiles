FROM openjdk:8-slim

ENV ES_VERSION 1.4.5
ENV ES_DOWNLOAD_SHA256 dc28aa9e441cbc3282ecc9cb498bea219355887b102aac872bdf05d5977356e2

RUN apt-get update && apt-get install -y --no-install-recommends curl && \
  curl -L -O https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz && \
  echo "$ES_DOWNLOAD_SHA256 elasticsearch-$ES_VERSION.tar.gz" | sha256sum -c && \
  tar -xvf elasticsearch-$ES_VERSION.tar.gz

CMD elasticsearch-$ES_VERSION/bin/elasticsearch
