FROM fluent/fluentd:v1.6.3-1.0
USER root
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.4.4/bin:$PATH

RUN set -ex \
    && apk update \
    && apk upgrade \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        ruby-dev \
        libffi-dev \
    && gem install -N \
        fluent-plugin-cloudwatch-logs:0.7.4 \
        fluent-plugin-kubernetes_metadata_filter:2.1.6 \
        fluent-plugin-prometheus:1.5.0 \
        fluent-plugin-rewrite-tag-filter:2.2.0 \
        ffi \
        fluent-plugin-systemd:1.0.2 \
        fluent-plugin-datacounter:1.0.0 \
    && apk del .build-deps \
    && gem sources --clear-all \
    && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

RUN apk add -U curl jq \
  && curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.5/bin/linux/amd64/kubectl \
  && chmod +x ./kubectl \
  && mv ./kubectl /usr/bin/kubectl

# Run Fluentd
ENTRYPOINT [ "fluentd", "-p", "/fluentd/plugins", "-c", "/etc/fluentd/fluent.conf" ]
