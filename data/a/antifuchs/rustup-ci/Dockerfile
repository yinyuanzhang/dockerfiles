FROM liuchong/rustup:nightly-onbuild
MAINTAINER Andreas Fuchs <asf@boinkor.net>

RUN apt-get update && apt-get install -y git && apt-get autoclean
RUN cargo install cargo-benchcmp --force
