FROM rustlang/rust:nightly

# Install packages required for building with musl
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        musl-tools \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add musl target to Rust toolchain
RUN rustup target add x86_64-unknown-linux-musl

# Update crates.io index
RUN cd /tmp && \
    env USER=root cargo new --bin registry-update && \
    cd /tmp/registry-update && \
    echo 'log = "0.4"' >> Cargo.toml && \
    cargo generate-lockfile && \
    cd / && \
    rm -fr /tmp/registry-update
