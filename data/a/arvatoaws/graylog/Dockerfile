FROM graylog/graylog:2.5.1

ADD --chown=graylog:graylog https://github.com/graylog-labs/graylog-plugin-metrics-reporter/releases/download/2.4.0-beta.3/metrics-reporter-prometheus-2.4.0-beta.3.jar /usr/share/graylog/plugin/metrics-reporter-prometheus-2.4.0-beta.3.jar

COPY docker-entrypoint.sh /
