FROM grauwoelfchen/gentoo-amd64-nomultilib:latest

LABEL maintainer="Yasuhiro Яша Asaka <yasuhiro.asaka@grauwoelfchen.net>"

ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH

WORKDIR /tmp

RUN set -eux && \
    \
    emerge -qv net-misc/curl

RUN set -eux && \
    \
    platform="x86_64-unknown-linux-gnu" && \
    url="https://static.rust-lang.org/rustup/dist/${platform}/rustup-init" && \
    curl -sSfLO "$url" && \
    chmod +x rustup-init && \
    ./rustup-init -y --no-modify-path --default-toolchain stable && \
    rm rustup-init && \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME && \
    rustup component add rust-src && \
    \
    rustup --version && \
    rustup show && \
    rustc --version && \
    cargo --version

WORKDIR /
CMD ["/bin/bash"]
