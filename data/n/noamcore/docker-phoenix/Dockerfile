FROM elixir:1.7.1-alpine
LABEL maintainer Iago S. <146050u54[at]gmail[dot]com>

# Installing Phoenix, Node, NPM and Yarn
RUN set -xe \
	&& apk add --no-cache \
		inotify-tools \
		nodejs-current \
		nodejs-npm \
		yarn \
	&& mix local.hex --force \
	&& mix local.rebar --force \
	&& mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phx_new.ez

WORKDIR /usr/share/html

VOLUME /usr/share/html

EXPOSE 4000

CMD ["mix", "phx.server"]

# vim: noet ts=4 sw=4
