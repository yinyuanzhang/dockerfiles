FROM golang:1.11.2-alpine3.8 AS build

RUN \
  apk add --no-cache \
    cairo-dev \
    gcc \
    git \
    make \
    musl-dev \
  \
  && mkdir -p src/github.com/go-graphite \
  && cd src/github.com/go-graphite \
  && git clone https://github.com/go-graphite/carbonapi \
  && cd carbonapi \
  && make

FROM alpine:3.8

COPY --from=build /go/src/github.com/go-graphite/carbonapi/carbonapi /usr/local/bin/carbonapi
COPY carbonapi.yml /etc/carbonapi.yml

RUN \
  adduser -DH user \
  \
  && apk add --no-cache \
    cairo

USER user

EXPOSE 8081

CMD ["/usr/local/bin/carbonapi", "-config", "/etc/carbonapi.yml", "-envprefix", "CARBONAPI"]
