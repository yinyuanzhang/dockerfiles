FROM quay.io/fluentd_elasticsearch/fluentd:v2.7.0

LABEL maintainer="siriuszg <zhigang52110@sina.com>"

RUN fluent-gem install fluent-plugin-webhdfs \
    && fluent-gem install fluent-plugin-kafka && fluent-gem cleanup

# RUN gem install fluentd --no-ri --no-rdoc && gem cleanup fluentd
# RUN fluent-gem install fluent-plugin-detect-exceptions \
#     && fluent-gem install fluent-plugin-multi-format-parser \
#     && fluent-gem install fluent-plugin-kubernetes_metadata_filter \
#     && fluent-gem install fluent-plugin-prometheus \
#     && fluent-gem install fluent-plugin-systemd \
#     && fluent-gem install fluent-plugin-elasticsearch \
#     && fluent-gem install fluent-plugin-webhdfs \
#     && fluent-gem install fluent-plugin-kafka && fluent-gem cleanup
