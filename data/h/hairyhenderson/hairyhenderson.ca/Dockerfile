FROM alpine:3.10

LABEL maintainer="Dave Henderson <dhenderson@gmail.com>"

RUN apk add --no-cache tar curl git
RUN curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
      "https://caddyserver.com/download/linux/amd64?plugins=http.git,http.gopkg,http.minify,http.prometheus,http.restic&license=personal&telemetry=on" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
  && chmod 0755 /usr/bin/caddy \
  && /usr/bin/caddy -version

EXPOSE 80 443
WORKDIR /srv

RUN mkdir /site

COPY Caddyfile /etc/Caddyfile
COPY index.md /srv/index.md
COPY *.html /srv/

ENTRYPOINT ["/usr/bin/caddy"]
CMD ["-agree", "-conf", "/etc/Caddyfile"]
