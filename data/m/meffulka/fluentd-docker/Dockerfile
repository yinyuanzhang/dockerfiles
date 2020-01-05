FROM fluent/fluentd

RUN apk add --update --virtual .build-deps sudo build-base git ruby-dev \
  && git clone https://github.com/LamCiuLoeng/fluent-plugin-color-stripper \
  && cd fluent-plugin-color-stripper \
  && fluent-gem build fluent-plugin-color-stripper.gemspec \
  && fluent-gem install fluent-plugin-color-stripper-0.0.3.gem \
  && cd .. \
  && sudo gem install fluent-plugin-rewrite-tag-filter \
  && sudo gem install fluent-plugin-geoip-filter \
  && sudo gem install fluent-plugin-record-modifier --no-document \
  && sudo gem install fluent-plugin-elasticsearch \
  && sudo gem sources --clear-all \
  && apk del .build-deps \
  && rm -rf fluent-plugin-color-stripper \
  && rm -rf /var/cache/apk/* /home/fluent/.gem/ruby/*/cache/*.gem

RUN mkdir -p /var/log/fluentd && chown 1000:1000 /var/log/fluentd/

EXPOSE 24224
