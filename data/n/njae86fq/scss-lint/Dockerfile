FROM debian:jessie

ENV APP_DIR=/opt/scss-lint

COPY Gemfile \
     Gemfile.lock \
     ${APP_DIR}/

RUN apt-get update \
 && RUNTIME_DEPS=' \
      ruby2.1 \
      rubygems \
    ' \
 && apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \
 && cd ${APP_DIR} \
 && gem install bundler --no-document \
 && (echo 'install: --no-document'; echo 'update: --no-document') > $HOME/.gemrc \
 && cd ${APP_DIR} \
 && bundle install \
 && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}

ENTRYPOINT ["scss-lint"]
CMD ["--help"]
