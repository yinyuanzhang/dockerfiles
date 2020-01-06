FROM debian:jessie

ENV APP_DIR=/opt/css2sass

COPY Gemfile.lock /tmp/

RUN apt-get update \
 && RUNTIME_DEPS=' \
      ruby2.1 \
      ruby2.1-dev \
      rubygems \
    ' \
    GIT_DEPS=' \
      ca-certificates \
      git \
    ' \
    OTHER_DEPS=' \
      build-essential \
      libssl-dev \
    ' \
    BUILD_DEPS="${GIT_DEPS} ${OTHER_DEPS}" \
    CSS2SASS_COMMIT_ID=0abbd569926dca1dde675326090f8da638eb9d81 \
 && apt-get install -y --no-install-recommends ${RUNTIME_DEPS} ${BUILD_DEPS} \
 && git clone https://github.com/jpablobr/css2sass ${APP_DIR} \
 && cd ${APP_DIR} \
 && git checkout ${CSS2SASS_COMMIT_ID} \
 && gem install bundler --no-document \
 && (echo 'install: --no-document'; echo 'update: --no-document') > $HOME/.gemrc \
 && cp -av /tmp/Gemfile.lock . \
 && bundle install \
 && apt-get purge -y ${BUILD_DEPS} \
 && apt-get autoremove -y \
 && apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \
 && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}

EXPOSE 5000

ENTRYPOINT ["foreman", "start"]
