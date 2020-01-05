FROM buildpack-deps:stretch

# Add wait-for.
RUN curl --output /bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/f71f8199a0dd95953752fb5d3f76f79ced16d47d/wait-for
RUN chmod +x /bin/wait-for
RUN wait-for --help

# Add node stuff.
ARG NODE_VERSION=node_9.x

# Install dependencies to install dependencies.
RUN apt-get update && apt-get install --yes \
  gnupg2 \
  apt-transport-https

# Add node repository.
RUN curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key \
    | apt-key add - && \
  echo "deb https://deb.nodesource.com/${NODE_VERSION} stretch main" \
    | tee /etc/apt/sources.list.d/nodesource.list && \
  echo "deb-src https://deb.nodesource.com/${NODE_VERSION} stretch main" \
    | tee --append /etc/apt/sources.list.d/nodesource.list

# Add yarn repository.
RUN curl --silent --show-error https://dl.yarnpkg.com/debian/pubkey.gpg \
    | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" \
    | tee /etc/apt/sources.list.d/yarn.list

# Install dependencies.
RUN apt-get update && \
  apt-get install --yes \
  nodejs \
  yarn \
  netcat-openbsd \
  cmake \
  clang-3.9 \
  zlib1g-dev

# Setup Rust variables and versions.
ARG rustToolchain='1.28.0'
ARG rustupVersion='1.13.0'
ARG rustupSha256='f69dafcca62fe70d7882113e21bb96a2cbdf4fc4636d25337d6de9191bdec8da'

ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    rustArch='x86_64-unknown-linux-gnu'

# Install Rust.
RUN set -eux; \
    url="https://static.rust-lang.org/rustup/archive/${rustupVersion}/${rustArch}/rustup-init"; \
    wget "$url"; \
    echo "${rustupSha256} *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --default-toolchain "${rustToolchain}"; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version;


# Install Diesel CLI
RUN cargo install diesel_cli --no-default-features --features "sqlite"

# Install rustfmt.
RUN rustup component add rustfmt-preview;
