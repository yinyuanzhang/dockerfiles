FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.3

RUN bin/elasticsearch-plugin install -b https://distfiles.compuscene.net/elasticsearch/elasticsearch-prometheus-exporter-6.4.3.0.zip
RUN bin/elasticsearch-plugin install -b com.floragunn:search-guard-6:6.4.3-23.1

# workaround to avoid file mounts
RUN mkdir -p /usr/share/elasticsearch/config/overrides \
  && mv /usr/share/elasticsearch/config/elasticsearch.yml /usr/share/elasticsearch/config/overrides \
  && ln -s /usr/share/elasticsearch/config/overrides/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
