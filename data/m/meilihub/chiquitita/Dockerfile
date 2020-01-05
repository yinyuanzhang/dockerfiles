FROM    ubuntu:16.04

RUN     apt update -y
RUN     apt install -y cmake \
                       clang \
                       curl \
                       pkg-config \
                       zlib1g-dev \
                       libssl-dev

RUN     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain nightly
ENV     PATH="$HOME/.cargo/bin:$PATH"

