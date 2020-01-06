ARG RUBY_VERSION=2.6.5

FROM ruby:${RUBY_VERSION}-alpine AS production
ARG RAILS_ENV=production

ENV RAILS_ENV $RAILS_ENV

RUN apk add --no-cache yarn postgresql-libs postgresql-client tzdata curl bash openssl

RUN addgroup -S www \
  && adduser -G www -S www
USER www
