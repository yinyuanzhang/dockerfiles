FROM ruby:2.5.3-alpine3.8

RUN apk add wkhtmltopdf \
  --update-cache \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  --allow-untrusted

RUN apk add --update git \
  build-base \
  curl-dev \
  libpq \
  postgresql-dev \
  postgresql-client \
  nodejs \
  file \
  tzdata

CMD [ "irb" ]
