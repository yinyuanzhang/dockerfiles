FROM ekidd/rust-musl-builder AS builder

ARG VERSION=1.4.1

RUN curl -L https://github.com/birkenfeld/fddf/archive/v$VERSION.tar.gz --output fddf.tar.gz \
    && tar -xvf fddf.tar.gz \
    && cd ./fddf-$VERSION/ \
    && cargo build --release


FROM alpine:3.8

LABEL org.label-schema.vcs-url="https://github.com/mrsaints/docker-fddf" \
      maintainer="Ian L. <os@fyianlai.com>"

ARG VERSION=1.4.1

COPY --from=builder \
    /home/rust/src/fddf-$VERSION/target/x86_64-unknown-linux-musl/release/fddf \
    /usr/local/bin/

WORKDIR /target/

CMD /usr/local/bin/fddf
