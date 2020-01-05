# @see https://circleci.com/docs/2.0/custom-images/ to push new versions
# Rust
FROM rust:latest
ENV PATH="${PATH}"

RUN rustup update nightly
RUN rustup default nightly
RUN rustup component add rustfmt-preview
RUN rustup target add wasm32-unknown-unknown

# Install mdbook
RUN curl -OL https://github.com/rust-lang-nursery/mdBook/releases/download/v0.2.1/mdbook-v0.2.1-x86_64-unknown-linux-gnu.tar.gz
RUN tar xf mdbook-v0.2.1-x86_64-unknown-linux-gnu.tar.gz
RUN rm mdbook-v0.2.1-x86_64-unknown-linux-gnu.tar.gz
RUN chmod +x mdbook
RUN mv mdbook /usr/local/bin/mdbook

# Install WASM bindgen CLI
RUN curl -OL https://github.com/rustwasm/wasm-bindgen/releases/download/0.2.31/wasm-bindgen-0.2.31-x86_64-unknown-linux-musl.tar.gz
RUN tar xf wasm-bindgen-0.2.31-x86_64-unknown-linux-musl.tar.gz
RUN rm wasm-bindgen-0.2.31-x86_64-unknown-linux-musl.tar.gz
RUN chmod +x wasm-bindgen-0.2.31-x86_64-unknown-linux-musl/wasm-bindgen
RUN mv wasm-bindgen-0.2.31-x86_64-unknown-linux-musl/wasm-bindgen /usr/local/bin/wasm-bindgen

RUN apt-get update

# build deps
RUN apt-get install -y unzip

# Git
RUN apt-get install -y git-core

# Postgres
RUN apt-get install sudo
RUN apt-get -y install postgresql postgresql-contrib

# Blender
# https://stackoverflow.com/a/26028597/3701114
RUN ln /dev/null /dev/raw1394
RUN apt-get install -y blender
RUN apt-get install -y imagemagick

# Node.js & npm
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs

# Build tools for making npm install work
RUN apt-get install -y build-essential
RUN apt-get install -y libssl-dev
RUN apt-get install -y pkg-config

# Geckodriver for wasm tests
RUN curl --retry 5 -LO https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
RUN tar xf geckodriver-v0.21.0-linux64.tar.gz
RUN mv geckodriver /usr/local/bin/

# Chromedriver for wasm tests
RUN curl --retry 5 -LO https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN export CHROMEDRIVER_ARGS=--verbose
RUN mv chromedriver /usr/local/bin/
