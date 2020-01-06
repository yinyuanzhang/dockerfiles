FROM docker.elastic.co/kibana/kibana:7.2.0
ENV XPACK_MONITORING_ENABLED true
ENV XPACK_MONITORING_UI_CONTAINER_ELASTICSEARCH_ENABLED true
ENV XPACK_REPORTING_ENABLED false
ENV XPACK_SECURITY_ENABLED false
ENV XPACK_WATCHER_ENABLED false
ENV XPACK_SPACES_ENABLED false
RUN /usr/share/kibana/bin/kibana-plugin install https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins/opendistro-security/opendistro_security_kibana_plugin-1.2.0.0.zip
RUN /usr/share/kibana/bin/kibana-plugin install https://d3g5vo6xdbdb9a.cloudfront.net/downloads/kibana-plugins/opendistro-alerting/opendistro-alerting-1.2.0.0.zip
RUN /usr/share/kibana/bin/kibana --optimize