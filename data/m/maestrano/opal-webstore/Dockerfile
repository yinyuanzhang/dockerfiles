# TODO: start direcly from ruby image?
FROM maestrano/web-ruby:2.3-v1.0.2
MAINTAINER developpers@maestrano.com

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/maestrano/opal-webstore" \
      org.label-schema.vendor="Maestrano" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# Cache folder
ENV YARN_CACHE_FOLDER /cache/yarn
ENV bower_storage__packages /cache/bower
ENV GEM_SPEC_CACHE /cache/gem

# Install yarn
ADD https://dl.yarnpkg.com/debian/pubkey.gpg /tmp/yarn-pubkey.gpg
RUN set -ex && \
    apt-key add /tmp/yarn-pubkey.gpg && rm /tmp/yarn-pubkey.gpg && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends yarn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# TODO: replace by `rake mnoe:frontend:install_dependencies`?
RUN yarn global add bower

RUN set -ex \
    && echo 'gem: --no-document' >> /etc/gemrc \
    && gem install bundler

WORKDIR /app
ADD Gemfile Gemfile.lock /app/

# Run bundle install as www-data to avoid chown
USER www-data

RUN set -ex \
    && export BUNDLE_JOBS=${BUNDLE_JOBS:-$(nproc)} \
    # default to number of cores
    && bundle install --deployment --without development test

USER root

COPY docker/docker-entrypoint.sh /usr/local/bin/

ADD --chown=www-data:www-data . /app

# Build frontend
RUN set -ex \
    && echo '{ "allow_root": true }' > /root/.bowerrc \
    && SECRET_KEY_BASE=secret bundle exec rake mnoe:frontend:build \
    && chown -R www-data:www-data /app/tmp /app/node_modules/ /app/public/dashboard/
