FROM abiosoft/caddy:latest
MAINTAINER Hyacinthus <hyacinthus@gmail.com>

ARG hugo_version=0.53

RUN apk add --no-cache openssh-client git tar curl

RUN curl --silent --show-error --fail --location \
  --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
  "https://github.com/gohugoio/hugo/releases/download/v${hugo_version}/hugo_${hugo_version}_Linux-64bit.tar.gz" \
  | tar --no-same-owner -C /tmp -xz \
  && mv /tmp/hugo /usr/bin/hugo \
  && chmod 0755 /usr/bin/hugo \
  && git config --global fetch.recurseSubmodules true \
  && mkdir -p /www/public

WORKDIR /www

COPY Caddyfile /etc/Caddyfile

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:80

ENV REPO github.com/hyacinthus/blog
