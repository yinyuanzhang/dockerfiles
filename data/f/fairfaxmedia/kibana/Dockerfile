FROM docker.elastic.co/kibana/kibana:6.7.1

ARG KIBANA_VERSION=6.7.1

RUN export NODE_OPTIONS="--max-old-space-size=1536" && \
    bin/kibana-plugin install https://github.com/pjhampton/kibana-prometheus-exporter/releases/download/${KIBANA_VERSION}/kibana-prometheus-exporter-${KIBANA_VERSION}.zip
