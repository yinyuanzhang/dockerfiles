FROM erlang:22-alpine

# elixir expects utf8.
ENV ELIXIR_VERSION="v1.8.2" \
	LANG=C.UTF-8

RUN set -xe \
	&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-lang/elixir/archive/${ELIXIR_VERSION}.tar.gz" \
	&& ELIXIR_DOWNLOAD_SHA256="cf9bf0b2d92bc4671431e3fe1d1b0a0e5125f1a942cc4fdf7914b74f04efb835" \
	&& buildDeps=' \
		ca-certificates \
		curl \
		make \
	' \
	&& apk add --no-cache --virtual .build-deps $buildDeps \
	&& curl -fSL -o elixir-src.tar.gz $ELIXIR_DOWNLOAD_URL \
	&& echo "$ELIXIR_DOWNLOAD_SHA256  elixir-src.tar.gz" | sha256sum -c - \
	&& mkdir -p /usr/local/src/elixir \
	&& tar -xzC /usr/local/src/elixir --strip-components=1 -f elixir-src.tar.gz \
	&& rm elixir-src.tar.gz \
	&& cd /usr/local/src/elixir \
	&& make install clean \
	&& apk del .build-deps

# install system dependencies
RUN apk update \
    && apk --no-cache --update add nodejs nodejs-npm openssl-dev build-base make gcc imagemagick \
    && mix local.rebar --force \
    && mix local.hex --force

# production mode
ENV MIX_ENV=prod \
    NODE_ENV=prod

# Where the elixir app should live
WORKDIR /opt/app

# warm up mix cache
COPY mix.exs .
COPY mix.lock .
RUN mix do deps.get, deps.compile

# warm up npm cache
COPY package.json ./apps/admin/assets/package.json
COPY package-lock.json ./apps/admin/assets/package-lock.json
RUN cd ./apps/admin/assets && npm ci

CMD ["iex"]
