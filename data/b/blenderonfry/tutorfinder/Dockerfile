FROM rust:latest AS builder
COPY Cargo.toml Cargo.lock /tmp/tutorsearch/
COPY src /tmp/tutorsearch/src/
WORKDIR /tmp/tutorsearch

RUN cargo build --release

FROM debian
ENV DEBIAN_FRONTEND noninteractive
COPY --from=builder /tmp/tutorsearch/target/release/tutorsearch .
COPY . .
RUN apt-get update && apt-get -y install libssl-dev libcurl4-openssl-dev
CMD ["./tutorsearch"]