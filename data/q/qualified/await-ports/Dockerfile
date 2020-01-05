FROM rust:1.38-alpine3.10 AS builder
# Do static build and strip symbols
RUN apk add --no-cache binutils
WORKDIR /workspace
COPY await-ports/Cargo.lock ./Cargo.lock
COPY await-ports/Cargo.toml ./Cargo.toml
COPY await-ports/src ./src
RUN set -ex; \
    cargo build --release --target x86_64-unknown-linux-musl; \
    strip ./target/x86_64-unknown-linux-musl/release/await-ports;


FROM alpine:3.10 AS tini-static
RUN apk add --no-cache tini-static


FROM scratch
COPY --from=tini-static /sbin/tini-static /tini
COPY --from=builder /workspace/target/x86_64-unknown-linux-musl/release/await-ports /await-ports
ENTRYPOINT ["/tini", "--", "/await-ports"]
