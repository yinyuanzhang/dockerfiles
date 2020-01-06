FROM rustlang/rust:nightly-slim as build

WORKDIR /usr/src/app

#COPY Cargo.toml Cargo.toml
#COPY Cargo.lock Cargo.lock

#RUN cargo build --release || true

#RUN rustup override set nightly-2018-05-30 # https://github.com/rust-lang-nursery/rust-clippy/issues/2482

# We need to add the source code to the image because `rust-musl-builder`
# assumes a UID of 1000, but TravisCI has switched to 2000.

ADD . ./

RUN cargo build --release; \
    rm -rf src/;

# ---------------------------

FROM debian:stretch-slim

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/target/release/recommend /usr/src/app/ 

EXPOSE 8000

ENV RUST_LOG info

CMD ["./recommend"]
