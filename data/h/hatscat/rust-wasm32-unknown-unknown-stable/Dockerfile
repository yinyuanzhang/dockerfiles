# inspired by jibbow/rust-wasm32-unknown-unknown
FROM rust

LABEL maintainer="Lucien Boudy"
LABEL version="1.0"
LABEL description="The Rust wasm32-unknown-unknown toolchain (stable) + cargo-make"

# install node.js (npm!)
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*
# add wasm target
RUN rustup update && rustup target add wasm32-unknown-unknown
# install additional wasm tools
RUN cargo install wasm-bindgen-cli && cargo install cargo-make
