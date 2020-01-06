FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.3
LABEL maintainer="chaya"

COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN bin/elasticsearch-plugin install ingest-attachment