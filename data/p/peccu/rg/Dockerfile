FROM alpine:latest as build
MAINTAINER Kentaro Shimatani <peccul@gmail.com>

ENV RG_VERSION=11.0.2
RUN set -x \
  && wget https://github.com/BurntSushi/ripgrep/releases/download/${RG_VERSION}/ripgrep-${RG_VERSION}-x86_64-unknown-linux-musl.tar.gz \
  && tar xzf ripgrep-${RG_VERSION}-x86_64-unknown-linux-musl.tar.gz \
  && mv ripgrep-${RG_VERSION}-x86_64-unknown-linux-musl/rg /rg

FROM alpine:latest

COPY --from=build /rg /usr/local/bin/

WORKDIR /app

VOLUME ["/app"]

CMD ["rg"]
