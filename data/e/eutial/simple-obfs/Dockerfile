FROM alpine:3.9 as builder
LABEL maintainer="Entrophy LLC"
RUN apk add --no-cache git \
    asciidoc \
    autoconf \
    automake \
    build-base \
    g++ \
    gcc \
    libev-dev \
    libpcre32 \
    libtool \
    linux-headers \
    make \
    openssl \
    xmlto \
    zlib-dev
RUN git clone https://github.com/shadowsocks/simple-obfs.git \
    && cd simple-obfs \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure \
    && make

FROM alpine:3.9
COPY --from=builder /simple-obfs/src/obfs-server /usr/bin/obfs-server
RUN apk add --no-cache libev
WORKDIR /etc/simple-obfs
CMD [ "obfs-server", "-c", "/etc/simple-obfs/config.json" ]