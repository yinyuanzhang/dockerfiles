FROM debian:stretch

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y curl file git pkg-config \
    gcc g++ make cmake automake openssh-client autoconf

# Install rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH "$PATH:/root/.cargo/bin"
# Needed for kcov
ENV RUSTFLAGS "-C link-dead-code"

# Update rust/install channels
RUN rustup update && \
    rustup install stable && \
    rustup install nightly && \
    rustup default stable

# Install rust dependencies
RUN rustup component add clippy && \
    rustup component add rustfmt && \
    rustup component add rustfmt --toolchain nightly