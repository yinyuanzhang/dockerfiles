FROM elixir:1.9.4-alpine

RUN apk add --no-cache \
  git \
  yarn \
  openssl \
  python3 \
  postgresql-client \
  build-base

RUN pip3 install awscli --upgrade

RUN adduser -S elixir

USER elixir

RUN mix local.hex --force \
  && mix local.rebar --force \
  && yes | mix archive.install hex sobelow
