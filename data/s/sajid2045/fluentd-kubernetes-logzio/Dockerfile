FROM fluent/fluentd-kubernetes-daemonset:v0.12-alpine-elasticsearch

# Ensure there are enough file descriptors for running Fluentd.
RUN ulimit -n 65536

COPY entrypoint.sh /fluentd/entrypoint.sh
RUN chmod +x /fluentd/entrypoint.sh

RUN fluent-gem install fluent-plugin-logzio
RUN fluent-gem install fluent-plugin-rewrite-tag-filter

COPY conf/fluent.conf /fluentd/etc/fluent.conf
COPY conf/kubernetes.conf /fluentd/etc/kubernetes.conf

CMD ["/fluentd/entrypoint.sh"]
