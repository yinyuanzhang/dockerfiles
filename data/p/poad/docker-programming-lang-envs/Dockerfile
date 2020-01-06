ARG PROTOCOL_BUFFERS_VERSION="3.11.2"

FROM buildpack-deps:stable-curl AS download

ARG PROTOCOL_BUFFERS_VERSION

WORKDIR /tmp

RUN curl -sSLo /tmp/llvm-snapshot.gpg.key https://apt.llvm.org/llvm-snapshot.gpg.key \
 && curl -sSLo /tmp/protobuf-all-${PROTOCOL_BUFFERS_VERSION}.tar.gz https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOCOL_BUFFERS_VERSION}/protobuf-all-${PROTOCOL_BUFFERS_VERSION}.tar.gz \
 && tar xf protobuf-all-${PROTOCOL_BUFFERS_VERSION}.tar.gz \
 && rm -f tar xf protobuf-all-${PROTOCOL_BUFFERS_VERSION}.tar.gz \
 && mv /tmp/protobuf-${PROTOCOL_BUFFERS_VERSION} /tmp/protobuf

FROM rust:slim AS build

ARG PROTOCOL_BUFFERS_VERSION

COPY --from=download /tmp/llvm-snapshot.gpg.key /tmp/llvm-snapshot.gpg.key
COPY --from=download /tmp/protobuf /tmp/protobuf

WORKDIR /tmp

RUN apt-get update -qq \
 && apt-get install --no-install-recommends -qqy ca-certificates gnupg2 binutils apt-utils \
 && cat /tmp/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-9 main" >> /etc/apt/sources.list.d/llvm-toolchain.list \
 && apt-get update -qq \
 && apt-get install -qqy --no-install-recommends \
        autoconf \
        automake \
        libtool \
        curl \
        make \
        clang-9 \
        lld-9 \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        unzip \
        zlib1g-dev \
        pkg-config \
        g++ \
        gcc \
        unzip \
        git \
        cmake \
        golang \
        libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /var/log/apt/* /var/log/alternatives.log /var/log/dpkg.log /var/log/faillog /var/log/lastlog \
 && cd /tmp/protobuf \
 && ./autogen.sh \
 && ./configure --prefix=/usr \
 && make \
 && make check \
 && make install \
 && ldconfig \
 && cd / \
 && rm -rf /tmp/*

