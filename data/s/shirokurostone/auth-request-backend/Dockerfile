FROM ruby:2.5.3-alpine

WORKDIR /usr/src/app
COPY . .
RUN apk add --no-cache --virtual=builddeps gcc libc-dev make linux-headers \
  && bundle install  \
  && apk del --purge builddeps \
  && adduser -S app \
  && chown -R app /usr/src/app
USER app

