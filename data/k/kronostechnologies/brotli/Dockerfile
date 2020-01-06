FROM alpine:latest as ssl
RUN apk add --update --no-cache ca-certificates

FROM gcc:7 as builder

RUN apt-get update && apt-get install cmake -y

ADD . /brotli
RUN mkdir -p /brotli/out
WORKDIR /brotli/out

RUN ../configure-cmake --disable-debug && make

FROM busybox:glibc

COPY --from=builder /brotli/out/brotli /bin/brotli
COPY --from=ssl /etc/ssl/certs /etc/ssl/certs
RUN mkdir -p /usr/bin && ln -s /bin/sh /usr/bin/sh
