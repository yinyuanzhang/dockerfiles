FROM rust:latest

ADD extra-cargo-conf /

RUN apt-get update && apt-get install -y \
    gcc-mingw-w64 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    rustup target add x86_64-pc-windows-gnu && \
    mkdir -p /usr/local/cargo && \
    bash -c 'cat /extra-cargo-conf >> /usr/local/cargo/config && rm /extra-cargo-conf'
