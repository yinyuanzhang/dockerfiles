FROM fluent/fluentd:v1.4-2

USER root

RUN apk add --no-cache git

RUN rm -rf /tmp/loki \
    && git clone --depth 1 https://github.com/grafana/loki.git /tmp/loki \
    && cd /tmp/loki/fluentd/fluent-plugin-loki \
    && sed -i "s|^  spec.files.*|  spec.files = Dir.glob('{bin,lib}/**/*')|" fluent-plugin-loki.gemspec \
    && gem build fluent-plugin-loki.gemspec \
    && gem install fluent-plugin-loki-*.gem \
    && cd /tmp \
    && rm -rf /tmp/loki

USER fluent