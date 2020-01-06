FROM fluent/fluentd:v0.12-onbuild-1
MAINTAINER Joachim Wickman <joachim@wickman.in>
WORKDIR /home/fluent
#ENV PATH /home/fluent/.gem/ruby/2.5.0/bin:$PATH

USER root
RUN apk --no-cache add sudo build-base ruby-dev geoip-dev libmaxminddb-dev && \
    gem install fluent-plugin-secure-forward \
        fluent-plugin-geoip fluent-plugin-record-modifier \
        fluent-plugin-beats fluent-plugin-forest \
        fluent-plugin-newsyslog fluent-plugin-elasticsearch \
        fluent-plugin-record-reformer fluent-plugin-parser \
        fluent-plugin-rewrite-tag-filter && \
#clean up
    rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem && \
    sudo -u fluent gem sources -c && \
    apk del sudo build-base ruby-dev

EXPOSE 24224 5140 5142 5044

VOLUME /fluentd/log

RUN mkdir -p /fluentd/etc/conf.user.d
COPY ["conf.d", "/fluentd/etc/conf.d/"]
USER fluent
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
