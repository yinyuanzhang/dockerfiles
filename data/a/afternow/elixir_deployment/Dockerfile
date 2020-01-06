FROM elixir:1.9.4

RUN apt-get update && apt-get install -y rsync

RUN mix local.rebar --force

RUN mix local.hex --force

CMD ["iex"]
