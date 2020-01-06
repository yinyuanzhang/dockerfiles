FROM rustlang/rust:nightly

RUN apt-get update && \
    apt-get install protobuf-compiler cmake -y && \
    cargo install cargo-audit

RUN rustup update && \
    rustup component add clippy-preview --toolchain=nightly

