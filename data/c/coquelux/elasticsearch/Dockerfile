FROM ubuntu:14.04

ENV ES_PKG_NAME elasticsearch-1.7.0

RUN apt-get update && \
    apt-get install -y openjdk-7-jre-headless wget vim-nox && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

VOLUME ["/data"]

ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

WORKDIR /data

EXPOSE 9200
EXPOSE 9300

CMD ["/elasticsearch/bin/elasticsearch"]
