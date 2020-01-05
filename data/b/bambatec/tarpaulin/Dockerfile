FROM rustlang/rust:nightly-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libssl-dev \
    pkg-config \
    cmake \
    zlib1g-dev \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/* \
  && RUSTFLAGS="--cfg procmacro2_semver_exempt" cargo install cargo-tarpaulin \
  && rustc -V \
  && cargo -V \
  && cargo tarpaulin -V
