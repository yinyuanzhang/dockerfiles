# Build this image: docker build -f .\Dockerfile -t illagrenan/pgloader .

FROM debian:stable-slim as builder
ARG PGLOADER_VERSION=master

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      bzip2 \
      ca-certificates \
      curl \
      freetds-dev \
      gawk \
      git \
      libsqlite3-dev \
      libssl1.1 \
      libzip-dev \
      make \
      openssl \
      patch \
      sbcl \
      time \
      unzip \
      wget \
      cl-ironclad \
      cl-babel \
    && rm -rf /var/lib/apt/lists/*


RUN git clone --branch ${PGLOADER_VERSION} --depth 1 https://github.com/dimitri/pgloader /opt/src/pgloader \
    && mkdir -p /opt/src/pgloader/build/bin \
    && cd /opt/src/pgloader \
    && make

FROM debian:stable-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      curl \
      freetds-dev \
      gawk \
      libsqlite3-dev \
      libzip-dev \
      make \
      sbcl \
      unzip \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/src/pgloader/build/bin/pgloader /usr/local/bin
