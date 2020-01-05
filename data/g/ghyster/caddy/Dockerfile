FROM alpine:3.6
MAINTAINER Nicolas Le Gras <nicolas.legras@gmail.com>

LABEL caddy_version="0.10.10" architecture="amd64"

ARG plugins=http.ipfilter,http.cors

RUN apk add --no-cache tar curl \
 && curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
      "https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
 && chmod 0755 /usr/bin/caddy \
 && /usr/bin/caddy -version

EXPOSE 80 443 2015
VOLUME /root/.caddy
VOLUME /var/www/html


ENTRYPOINT ["/usr/bin/caddy"]
CMD ["-quic","--conf", "/etc/Caddyfile", "--log", "stdout"]
