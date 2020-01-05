FROM alpine:3.6

MAINTAINER evuez <helloevuez@gmail.com>

ENV APP_HOME /app

RUN apk add --no-cache --update \
      bash git \
      make gcc g++ libc-dev inotify-tools \
      elixir \
      erlang-dev erlang-crypto erlang-syntax-tools erlang-dev erlang-sasl erlang-tools erlang-parsetools erlang-runtime-tools

RUN mix local.hex --force
RUN mix local.rebar --force

WORKDIR $APP_HOME

CMD ["iex", "-S", "mix"]

