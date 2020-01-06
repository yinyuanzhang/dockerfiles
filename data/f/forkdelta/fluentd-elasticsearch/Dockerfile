# cf. https://github.com/fluent/fluentd-docker-image#3-customize-dockerfile-to-install-plugins-optional
FROM fluent/fluentd:v1.1-onbuild

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-elasticsearch \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem

