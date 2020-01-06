FROM elixir:1.6.5-alpine
MAINTAINER dyoshikawa

RUN mix local.hex --force
RUN mix archive.install https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force
RUN mix local.rebar --force

RUN mix phx.new /myproject --no-brunch
WORKDIR /myproject
RUN mix deps.get

CMD mix phoenix.server
