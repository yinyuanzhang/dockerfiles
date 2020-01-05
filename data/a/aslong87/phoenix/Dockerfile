FROM aslong87/elixir:latest
MAINTAINER Andrew Long <aslong87@gmail.com>

RUN apt-get update && apt-get install -y curl

RUN curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash -

RUN apt-get update && apt-get install -y \
  git \
  nodejs \
  inotify-tools

RUN mix archive.install https://github.com/phoenixframework/phoenix/releases/download/v1.0.3/phoenix_new-1.0.3.ez --force

ONBUILD WORKDIR /app

ONBUILD COPY *.js* /app/
ONBUILD RUN npm install

ONBUILD ENV MIX_ENV prod
ONBUILD COPY mix.* /app/
ONBUILD COPY config /app/
ONBUILD RUN mix do deps.get, deps.compile
