# ===
# https://medium.com/@lemuelbarango/ruby-on-rails-smaller-docker-images-bff240931332
# ===

FROM ruby:2.6.3-alpine3.10 AS build-env

ARG RAILS_ROOT=/app
ARG BUILD_PACKAGES="build-base curl-dev git"
ARG DEV_PACKAGES="mariadb-connector-c-dev yaml-dev zlib-dev nodejs yarn python"
ARG RUBY_PACKAGES="tzdata"
ENV RAILS_ENV=production
ENV NODE_ENV=production
ENV BUNDLE_APP_CONFIG="$RAILS_ROOT/.bundle"
ENV RAILS_SERVE_STATIC_FILES=true

WORKDIR $RAILS_ROOT

# install packages
RUN apk update \
  && apk upgrade \
  && apk add --update --no-cache $BUILD_PACKAGES $DEV_PACKAGES $RUBY_PACKAGES

COPY Gemfile* package.json yarn.lock ./

# install rubygem
COPY Gemfile Gemfile.lock $RAILS_ROOT/

RUN bundle config --global frozen 1 \
  && bundle install --without development:test:assets -j4 --retry 3 --path=vendor/bundle \
  # Remove unneeded files (cached *.gem, *.o, *.c)
  && rm -rf vendor/bundle/ruby/2.6.0/cache/*.gem \
  && find vendor/bundle/ruby/2.6.0/gems/ -name "*.c" -delete \
  && find vendor/bundle/ruby/2.6.0/gems/ -name "*.o" -delete

RUN yarn install --production

COPY . .

# RUN bin/rails webpacker:compile
RUN bin/rails assets:precompile

# Remove folders not needed in resulting image
RUN rm -rf node_modules tmp/cache app/assets vendor/assets spec

############### Build step done ###############
FROM ruby:2.6.3-alpine3.10

ARG RAILS_ROOT=/app
ARG PACKAGES="tzdata nodejs bash mariadb-connector-c-dev"
ENV RAILS_ENV=production
ENV BUNDLE_APP_CONFIG="$RAILS_ROOT/.bundle"
ENV SECRET_KEY_BASE=7b1ba7b6d7a69c8c774615a188b122ff2f115edecf34235d1135e34335c69eb4359f825fd421564073691589a17cd8305d20cbaa8f8f19c5c2b8452dea55f395

WORKDIR $RAILS_ROOT

# install packages
RUN apk update \
  && apk upgrade \
  && apk add --update --no-cache $PACKAGES

COPY --from=build-env $RAILS_ROOT $RAILS_ROOT
EXPOSE 80

CMD ["bin/rails", "server", "-b", "0.0.0.0", "-p", "80"]
# CMD ["bash"]
