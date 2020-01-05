FROM alvarolizama/elixir:alpine-3.9
MAINTAINER Alvaro Lizama <me@alvarolizama.net>
RUN apk --no-cache add -U nodejs nodejs-npm inotify-tools libsass libsass-dev sassc \
    && mix archive.install hex phx_new 1.4.5 --force
