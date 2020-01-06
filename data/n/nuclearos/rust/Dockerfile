FROM debian:stretch

RUN apt-get update -q -y && apt-get -q -y install curl wget git gcc make qemu

RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly -y

ENV PATH "$PATH:/root/.cargo/bin"
ENV RUSTFLAGS "-C link-dead-code"
ENV CFG_RELEASE_CHANNEL "nightly"

RUN rustup update && rustup component add rust-src

RUN cargo install cargo-xbuild bootimage
RUN cargo install rustfmt-nightly --force
RUN rustup component add clippy-preview

RUN bash -l -c 'echo $(rustc --print sysroot)/lib >> /etc/ld.so.conf'
RUN bash -l -c 'echo /usr/local/lib >> /etc/ld.so.conf'
RUN ldconfig
