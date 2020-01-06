FROM fluent/fluentd:v1.7-1

USER root

RUN apk add --no-cache --update --virtual .build-deps \
    sudo build-base ruby-dev \
    && sudo gem install \
    fluent-plugin-elasticsearch \
    fluent-plugin-route \
    fluent-plugin-sumologic_output \
    && sudo gem sources --clear-all \
    && apk del .build-deps \
    && rm -rf /home/fluent/.gem/ruby/2.5.0/cache/*.gem

RUN apk add --no-cache git openssh-client

RUN mkdir /var/log/td-agent && chown fluent:fluent /var/log/td-agent

USER fluent