FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4

MAINTAINER Lukas Stefaniak <lstefaniak@globalwebindex.net>

ENV ES_NODE_MASTER=true
ENV ES_NODE_DATA=true
ENV ES_NODE_INGEST=true
ENV ES_HOST=0.0.0.0
ENV ES_NETWORK_HOST=0.0.0.0
ENV ES_PUBLISH_HOST=localhost
ENV ES_PUBLISH_PORT=9200

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin remove x-pack && \
    /usr/share/elasticsearch/bin/elasticsearch-plugin install discovery-ec2 && \
    /usr/share/elasticsearch/bin/elasticsearch-plugin install -b https://distfiles.compuscene.net/elasticsearch/elasticsearch-prometheus-exporter-6.2.4.0.zip

ADD config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
USER root
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml
USER elasticsearch




