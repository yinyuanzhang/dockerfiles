FROM centos:7

ENV RUST_VERSION 1.34.2
ENV HOME /home
ENV CARGO_HOME /usr/local/cargo
ENV PATH $CARGO_HOME/bin:$HOME/.cargo/bin:$PATH

RUN mkdir -p "$CARGO_HOME"
RUN curl -sSf https://sh.rustup.rs \
  | env -u CARGO_HOME sh -s -- -y --default-toolchain "$RUST_VERSION"
RUN rustup --version; \
    rustc --version; \
    cargo --version;

WORKDIR $HOME
