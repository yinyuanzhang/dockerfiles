FROM ubuntu:18.04

ARG RUST_TOOLCHAIN=nightly-2019-09-15
ARG RUST_USER=docker

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git git-lfs python3 python3-setuptools python3-wheel python3-pip python3-virtualenv curl

# Switching to local user
RUN useradd -ms /bin/bash $RUST_USER
USER $RUST_USER
WORKDIR /home/$RUST_USER/

# Python environment for Rust
ENV VIRTUAL_ENV=/home/$RUST_USER/rust-env/
RUN python3 -m virtualenv $VIRTUAL_ENV -p python3
ENV PATH=$VIRTUAL_ENV/bin:$PATH
RUN pip install setuptools-rust

# Installing Rust toolchain
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain $RUST_TOOLCHAIN
ENV PATH=/home/$RUST_USER/.cargo/bin:$PATH

# Installing AWS CLI tools
RUN pip install awscli s3pypi

ENTRYPOINT bash