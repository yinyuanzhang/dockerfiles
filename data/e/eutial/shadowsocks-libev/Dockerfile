FROM alpine:3.9 as builder
LABEL maintainer="Entrophy LLC"
RUN apk add --no-cache \
      asciidoc \
      autoconf \
      automake \
      build-base \
      c-ares-dev \
      git \
      libev-dev \
      libtool \
      libsodium-dev \
      linux-headers \
      mbedtls-dev \
      pcre-dev \
      xmlto
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git \
    && cd shadowsocks-libev \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure \
    && make

FROM alpine:3.9
COPY --from=builder /shadowsocks-libev/src/ss-server /usr/bin/ss-server
RUN apk add --no-cache libev \
            libsodium \
            mbedtls \
            pcre \
            c-ares \
            haveged
WORKDIR /etc/shadowsocks-libev
CMD [ "ss-server", "-c", "/etc/shadowsocks-libev/config.json" ]