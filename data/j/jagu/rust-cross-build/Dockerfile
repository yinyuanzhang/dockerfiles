FROM jagu/rust-cross-build:stable-x86_64-unknown-linux-gnu

RUN rustup component add clippy rustfmt \
    && rustup target add wasm32-unknown-unknown