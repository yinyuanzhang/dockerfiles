FROM alpine:3.10.3
MAINTAINER Mayank Pundir <mayank.pundir@razorpay.com>
LABEL Description="Fluentd docker image for aggregator nodes" Vendor="Fluent Organization" Version="1.5.0"

RUN apk update \
 && apk add --no-cache \
        ca-certificates \
        ruby ruby-irb ruby-etc ruby-webrick \
        tini xz su-exec \
 && apk add --no-cache --virtual .build-deps \
        build-base \
        ruby-dev gnupg \
 && echo 'gem: --no-document' >> /etc/gemrc \
 && gem install oj -v 3.3.10 \
 && gem install json -v 2.2.0 \
 && gem install fluentd -v 1.5.0 \
 && gem install bigdecimal -v 1.3.5 \
 && gem install fluent-plugin-s3 -v 1.0.0 \
 && gem install fluent-plugin-kubernetes_sumologic -v 2.4.2 \
 && gem install fluent-plugin-sumologic_output -v 1.6.1 \
 && gem install fluent-plugin-record-modifier -v 2.0.1 \
 && gem install fluent-plugin-rewrite-tag-filter -v 2.2.0 \
 && gem install prometheus-client -v 0.9.0 \
 && gem install fluent-plugin-prometheus -v 1.6.1 \
 && apk del .build-deps \
 && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

RUN addgroup -S fluent && adduser -S -g fluent fluent \
    && mkdir -p /fluentd/log \
    && mkdir -p /fluentd/etc /fluentd/plugins \
    && chown -R fluent /fluentd && chgrp -R fluent /fluentd


COPY fluent.conf /fluentd/etc/
COPY conf.d /fluentd/conf.d/
COPY entrypoint.sh /bin/


ENV PROM_CLUSTER_ENV="cluster-env"
ENV FLUENTD_CONF="fluent.conf"
ENV LOGS_ARCHIVE_FORMAT="gzip"
ENV SUMO_VERIFY_SSL="true"
ENV OUTPUT_BUFFER_PATH="/fluentd/buffers"
ENV NUM_FLUENTD_WORKERS="2"

ENV S3_TIME_KEY="1m"

# Whitelist for journald logs; on cluster-env
ENV SUMO_SYSTEMD_INCLUDE_CLUSTER_REGEX="/^(.+)$/"
ENV S3_SYSTEMD_INCLUDE_CLUSTER_REGEX="/^(.+)$/"

# Whitelist for k8s containers logs; on cluster-env & k8s.ns
ENV SUMO_CONTAINERS_INCLUDE_CLUSTER_REGEX="/^(.+)$/"
ENV S3_CONTAINERS_INCLUDE_CLUSTER_REGEX="/^(.+)$/"
ENV SUMO_CONTAINERS_INCLUDE_NS_REGEX="/^(.+)$/"
ENV S3_CONTAINERS_INCLUDE_NS_REGEX="/^(.+)$/"
ENV K8S_SUMO_SOURCE_CATEGORY_JOURNAL="k8s/journal"

ENV S3_FLUSH_THREAD_COUNT="2"

ENV EU_SUMO_COLLECTOR_URL_STAGE_WHITE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV EU_SUMO_COLLECTOR_URL_STAGE_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV EU_SUMO_COLLECTOR_URL_PROD_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV EU_SUMO_COLLECTOR_URL_PROD_BLUE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV EU_SUMO_COLLECTOR_URL_CDE_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV EU_SUMO_COLLECTOR_URL_CDE_BLUE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_STAGE_WHITE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_STAGE_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_PROD_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_PROD_BLUE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_CDE_GREEN="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="
ENV MUM_SUMO_COLLECTOR_URL_CDE_BLUE="https://endpoint1.collection.eu.sumologic.com/receiver/v1/http/placeholder-url=="

ENV SUMO_NUM_THREADS="2"
ENV SUMO_ADD_TIMESTAMP="true"
ENV SUMO_FLUSH_MODE="interval"
ENV SUMO_FLUSH_THREAD_COUNT="2"
ENV SUMO_FLUSH_INTERVAL="4s"


ENV LD_PRELOAD=""

EXPOSE 24224 5140 17171

# Needed for doing chown on a root-owned mount
#USER fluent
ENTRYPOINT ["tini",  "--", "/bin/entrypoint.sh"]
CMD ["fluentd"]

