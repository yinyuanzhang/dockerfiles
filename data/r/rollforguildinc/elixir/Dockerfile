FROM elixir:alpine

RUN apk --no-cache add --virtual build-base ca-certificates g++ make openssl openssh rsync

RUN mix local.hex --force
RUN mix local.rebar --force
