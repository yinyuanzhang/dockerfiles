FROM debian:stretch

ARG uid=1000
ARG version=1.32.0

# Base system

RUN apt-get update   && \
    DEBIAN_FRONTEND=noninteractive \
      apt-get install -y \
        build-essential  \
        ca-certificates  \
        libssl-dev       \
        pkg-config       \
        inotify-tools && \
    apt-get clean

ADD https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init /usr/local/bin/rustup-init
RUN chmod +x /usr/local/bin/rustup-init

ADD watch_and_run /usr/local/bin/watch_and_run

ENV RUSTUP_HOME /opt/multirust
ENV RUSTUP_TOOLCHAIN $version
ENV CARGO_HOME /host/volume/cargo
ENV PATH $PATH:/opt/rust/bin:$CARGO_HOME/bin

RUN CARGO_HOME=/opt/rust rustup-init -y --no-modify-path --default-toolchain $RUSTUP_TOOLCHAIN
RUN CARGO_HOME=/opt/rust rustup component add rustfmt
RUN CARGO_HOME=/opt/rust cargo install cargo-edit
RUN rm -rf /opt/rust/registry

# User configuration

RUN useradd -m -u $uid app
ENV USER app
