FROM rustlang/rust:nightly-slim
RUN rustup target add wasm32-unknown-unknown --toolchain nightly && cargo +nightly install --git https://github.com/alexcrichton/wasm-gc && rustup default nightly

ENV RUST_BACKTRACE 1
ENV CC gcc
ENV CXX g++
