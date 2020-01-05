# vim:set ft=dockerfile:

# Examples how to build for different architectures:
#docker build --build-arg TARGETPLATFORM=linux/amd64 --build-arg ARCH_REPO=amd64 --build-arg MUSL_ARCH=x86_64 --build-arg RUST_TARGET=x86_64-unknown-linux-musl --build-arg MUSL_INCLUDE_DIR=x86_64-linux-musl --build-arg GNU_INCLUDE_DIR=x86_64-linux-gnu --build-arg SSL_ARCH=linux-x86_64 .
#docker build --build-arg TARGETPLATFORM=linux/arm --build-arg ARCH_REPO=arm32v7 --build-arg MUSL_ARCH=armhf --build-arg RUST_TARGET=armv7-unknown-linux-musleabihf --build-arg MUSL_INCLUDE_DIR=arm-linux-musleabihf --build-arg GNU_INCLUDE_DIR=arm-linux-gnueabihf --build-arg SSL_ARCH=linux-generic32 .
#docker build --build-arg TARGETPLATFORM=linux/arm64 --build-arg ARCH_REPO=arm64v8 --build-arg MUSL_ARCH=aarch64 --build-arg RUST_TARGET=aarch64-unknown-linux-musl --build-arg MUSL_INCLUDE_DIR=aarch64-linux-musl --build-arg GNU_INCLUDE_DIR=aarch64-linux-gnu --build-arg SSL_ARCH=linux-aarch64 .

ARG TARGETPLATFORM=linux/amd64
ARG ARCH_REPO=amd64
#--platform=${TARGETPLATFORM}
FROM ${ARCH_REPO}/ubuntu

LABEL maintainer="Jens Keiner <jens@nfft.org>"

COPY qemu-arm-static /usr/bin
COPY qemu-aarch64-static /usr/bin

# Required packages:
# - musl-dev, musl-tools - the musl toolchain
# - curl, g++, make, pkgconf, cmake - for fetching and building third party libs
# - ca-certificates - openssl + curl + peer verification of downloads
# - xutils-dev - for openssl makedepend
# - libssl-dev and libpq-dev - for dynamic linking during diesel_codegen build process
# - git - cargo builds in user projects
# - linux-headers-amd64 - needed for building openssl 1.1 (stretch only)
# - file - needed by rustup.sh install
# - automake autoconf libtool - support crates building C deps as part cargo build
# recently removed:
# cmake (not used), nano, zlib1g-dev
RUN apt-get -y update && apt-get -y install \
  musl-dev \
  musl-tools \
  file \
  git \
  openssh-client \
  make \
  g++ \
  curl \
  pkgconf \
  ca-certificates \
  xutils-dev \
  libssl-dev \
  libpq-dev \
  automake \
  autoconf \
  libtool \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*

# Install rust using rustup
ARG CHANNEL="nightly"
ARG MUSL_ARCH=x86_64
ARG RUST_TARGET=x86_64-unknown-linux-musl
ARG MUSL_INCLUDE_DIR=x86_64-linux-musl
ARG GNU_INCLUDE_DIR=x86_64-linux-gnu
ARG SSL_ARCH=linux-x86_64
RUN curl https://sh.rustup.rs -sSf | \
    sh -s -- -y --default-toolchain ${CHANNEL} && \
    ~/.cargo/bin/rustup target add ${RUST_TARGET} && \
    echo "[build]\ntarget = \"${RUST_TARGET}\"" > ~/.cargo/config

# Convenience list of versions and variables for compilation later on
# This helps continuing manually if anything breaks.
ENV SSL_VER="1.0.2s" \
    CURL_VER="7.65.3" \
    ZLIB_VER="1.2.11" \
    PQ_VER="10.10" \
    SQLITE_VER="3290000" \
    CC=musl-gcc \
    PREFIX=/musl \
    PATH=/usr/local/bin:/root/.cargo/bin:$PATH \
    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \
    LD_LIBRARY_PATH=$PREFIX

# Set up a prefix for musl build libraries, make the linker's job of finding them easier
# Primarily for the benefit of postgres.
# Lastly, link some linux-headers for openssl 1.1 (not used herein)
RUN mkdir $PREFIX && \
    echo "$PREFIX/lib" >> /etc/ld-musl-${MUSL_ARCH}.path && \
    ln -s /usr/include/${GNU_INCLUDE_DIR}/asm /usr/include/${MUSL_INCLUDE_DIR}/asm && \
    ln -s /usr/include/asm-generic /usr/include/${MUSL_INCLUDE_DIR}/asm-generic && \
    ln -s /usr/include/linux /usr/include/${MUSL_INCLUDE_DIR}/linux

# Build zlib (used in openssl and pq)
RUN curl -sSL https://zlib.net/zlib-$ZLIB_VER.tar.gz | tar xz && \
    cd zlib-$ZLIB_VER && \
    CC="musl-gcc" LDFLAGS="-L$PREFIX/lib" CFLAGS="-I$PREFIX/include -fPIC -pie" ./configure --static --prefix=$PREFIX && \
    make -j$(nproc) && make install && \
    cd .. && rm -rf zlib-$ZLIB_VER

# # Build openssl (used in curl and pq)
# # Would like to use zlib here, but can't seem to get it to work properly
# # TODO: fix so that it works
# RUN curl -sSL https://www.openssl.org/source/openssl-$SSL_VER.tar.gz | tar xz && \
#     cd openssl-$SSL_VER && \
#     ./Configure no-zlib no-shared -fPIC --prefix=$PREFIX --openssldir=$PREFIX/ssl ${SSL_ARCH} && \
#     env C_INCLUDE_PATH=$PREFIX/include make depend 2> /dev/null && \
#     make -j$(nproc) && make install && \
#     cd .. && rm -rf openssl-$SSL_VER
#
# # Build curl (needs with-zlib and all this stuff to allow https)
# # curl_LDFLAGS needed on stretch to avoid fPIC errors - though not sure from what
# RUN curl -sSL https://curl.haxx.se/download/curl-$CURL_VER.tar.gz | tar xz && \
#     cd curl-$CURL_VER && \
#     CC="musl-gcc" LDFLAGS="-L$PREFIX/lib" CPPFLAGS="-I$PREFIX/include -fPIC -pie" ./configure \
#       --disable-shared --with-zlib=$PREFIX --with-ssl=$PREFIX --enable-optimize --prefix=$PREFIX \
#       --with-ca-path=/etc/ssl/certs/ --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt --without-ca-fallback && \
#     make -j$(nproc) curl_LDFLAGS="-all-static" && make install && \
#     cd .. && rm -rf curl-$CURL_VER
#
# # Build libpq
# RUN curl -sSL https://ftp.postgresql.org/pub/source/v$PQ_VER/postgresql-$PQ_VER.tar.gz | tar xz && \
#     cd postgresql-$PQ_VER && \
#     CC="musl-gcc" LDFLAGS="-L$PREFIX/lib" CFLAGS="-I$PREFIX/include -fPIE -pie" ./configure \
#     --without-readline \
#     --with-openssl \
#     --with-libraries=$PREFIX/lib \
#     --with-includes=$PREFIX/include \
#     --oldincludedir=/usr/include \
#     --prefix=$PREFIX --host=${RUST_TARGET} && \
#     cd src/interfaces/libpq make -s -j$(nproc) all-static-lib && make -s install install-lib-static && \
#     cd ../../bin/pg_config && make -j $(nproc) && make install && \
#     cd .. && rm -rf postgresql-$PQ_VER
#
# # Build libsqlite3 using same configuration as the alpine linux main/sqlite package
# RUN curl -sSL https://www.sqlite.org/2019/sqlite-autoconf-$SQLITE_VER.tar.gz | tar xz && \
#     cd sqlite-autoconf-$SQLITE_VER && \
#     CFLAGS=" -fPIC -pie -DSQLITE_ENABLE_FTS4 -DSQLITE_ENABLE_FTS3_PARENTHESIS -DSQLITE_ENABLE_FTS5 -DSQLITE_ENABLE_COLUMN_METADATA -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_RTREE -DSQLITE_USE_URI -DSQLITE_ENABLE_DBSTAT_VTAB -DSQLITE_ENABLE_JSON1" \
#     CC="musl-gcc" \
#     ./configure --prefix=$PREFIX --host=${RUST_TARGET} --enable-threadsafe --enable-dynamic-extensions --disable-shared && \
#     make && make install && \
#     cd .. && rm -rf sqlite-autoconf-$SQLITE_VER

# SSL cert directories get overridden by --prefix and --openssldir
# and they do not match the typical host configurations.
# The SSL_CERT_* vars fix this, but only when inside this container
# musl-compiled binary must point SSL at the correct certs (muslrust/issues/5) elsewhere
# Postgres bindings need vars so that diesel_codegen.so uses the GNU deps at build time
# but finally links with the static libpq.a at the end.
# It needs the non-musl pg_config to set this up with libpq-dev (depending on libssl-dev)
# See https://github.com/sgrif/pq-sys/pull/18
ENV PATH=$PREFIX/bin:$PATH \
    PKG_CONFIG_ALLOW_CROSS=true \
    PKG_CONFIG_ALL_STATIC=true \
    PQ_LIB_STATIC_X86_64_UNKNOWN_LINUX_MUSL=true \
    PQ_LIB_STATIC_ARMV7_UNKNOWN_LINUX_MUSLABIHF=true \
    PQ_LIB_STATIC_AARCH64_UNKNOWN_LINUX_MUSL=true \
    PQ_LIB_STATIC=true \
    PQ_LIB_DIR=$PREFIX/lib/ \
    PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig \
    PG_CONFIG_X86_64_UNKNOWN_LINUX_MUSL=/usr/bin/pg_config \
    PG_CONFIG_ARMV7_UNKNOWN_LINUX_MUSLABIHF=/usr/bin/pg_config \
    PG_CONFIG_AARCH64_UNKNOWN_LINUX_MUSL=/usr/bin/pg_config \
    OPENSSL_STATIC=true \
    OPENSSL_DIR=$PREFIX \
    OPENSSL_LIB_DIR=$PREFIX/lib/ \
    OPENSSL_INCLUDE_DIR=$PREFIX/include \
    DEP_OPENSSL_INCLUDE=$PREFIX/include/ \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_DIR=/etc/ssl/certs \
    LIBZ_SYS_STATIC=1 \
    TARGET=musl

# Allow ditching the -w /volume flag to docker run
WORKDIR /volume
