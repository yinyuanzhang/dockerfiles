FROM ruby:2.6.5-alpine

# Build-time metadata as defined at http://label-schema.org

RUN apk --no-cache add  build-base \
                        postgresql-dev \
                        tzdata \
                        nodejs \
                        yarn \
                        vips-dev \
                        git

ENV LANG=C.UTF-8 \
    APP_HOME=/it52
ENV BUNDLE_PATH=$APP_HOME/vendor/bundle \
    BUNDLE_JOBS=24 \
    BUNDLE_RETRY=3
ENV PATH=it52/bin:$BUNDLE_PATH/bin:$PATH

# Install latest rubygems, bundler and rake
RUN gem update --system && gem install bundler rake pry

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY Gemfile* $APP_HOME/
RUN bundle install

COPY package.json yarn.lock $APP_HOME/
RUN yarn install

ADD . $APP_HOME

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="IT52" \
      org.label-schema.description="IT52 rails application" \
      org.label-schema.url="https://www.it52.info" \
      org.label-schema.maintainer="Nick Kugaevsky \"nick@kugaevsky.ru\"" \
      org.label-schema.usage="README.md" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/nnrug/it52-rails" \
      org.label-schema.vendor="IT52" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

CMD ["bundle", "exec", "rails", "console"]
