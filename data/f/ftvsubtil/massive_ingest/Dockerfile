FROM elixir:1.7.3-alpine AS ex_builder

RUN apk update && \
    apk add --no-cache \
    ca-certificates \
    curl \
    gawk \
    git \
    make \
    nodejs \
    python \
    tar \
    wget \
    g++ \
    && \
    mix local.hex --force && \
    mix local.rebar --force && \
    mix hex.info && \
    cd /usr/local/bin && \
    curl -o- -L https://yarnpkg.com/install.sh | sh -s -- --version 1.9.4

WORKDIR /app
ENV MIX_ENV prod
ENV PATH /root/.yarn/bin:/root/.config/yarn/global/node_modules/.bin:$PATH
ADD . .

RUN mix deps.get && \
    mix release.init && \
    mix release --env=$MIX_ENV && \
    mix phx.digest

FROM alpine:3.8

WORKDIR /app

RUN apk update && \
    apk add bash openssl

COPY --from=ex_builder /app/_build/prod/rel/massive_ingest .

CMD ["./bin/massive_ingest", "foreground"]
