FROM docker.elastic.co/elasticsearch/elasticsearch:7.1.0

ENV ES_PROMETHEUS_EXPORTER_VERSION 7.1.0.0

# Install Prometheus plug-in
RUN elasticsearch-plugin install --batch https://github.com/vvanholl/elasticsearch-prometheus-exporter/releases/download/${ES_PROMETHEUS_EXPORTER_VERSION}/prometheus-exporter-${ES_PROMETHEUS_EXPORTER_VERSION}.zip