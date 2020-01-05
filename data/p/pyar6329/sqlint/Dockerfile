FROM ruby:2.6.5-alpine3.10

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN set -ex && \
  apk add --no-cache --virtual .build-tool build-base && \
  gem install sqlint && \
  apk del .build-tool && \
  rm -rf /var/cache/apk/* && \
  chmod +x /usr/local/bin/entrypoint.sh

ENV WORKSPACE=/workspace
WORKDIR ${WORKSPACE}

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
