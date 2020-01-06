FROM debian:buster

# install packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential autoconf libtool pkg-config make automake g++ \
    ca-certificates netbase wget unzip git curl libgflags-dev libgtest-dev \
    zlib1g-dev clang libc++-dev \
  && rm -rf /var/lib/apt/lists/*

# build and install grpc
ENV GRPC_RELEASE_TAG v1.20.0

RUN echo "==================== cloning repository ====================" \
  && git clone -b ${GRPC_RELEASE_TAG} https://github.com/grpc/grpc /var/local/git/grpc \
  && cd /var/local/git/grpc \
  && git submodule update --init \
  && echo "==================== installing protobuf ====================" \
  && cd third_party/protobuf \
  && ./autogen.sh \
  && ./configure --enable-shared --with-gnu-ld --with-zlib \
  && make -j$(nproc) \
  && make install \
  && make clean \
  && ldconfig \
  && echo "==================== installing grpc ====================" \
  && cd /var/local/git/grpc \
  && export CFLAGS=-Wno-error \
  && export CXXFLAGS=-Wno-error \
  && make -j$(nproc) \
  && make install \
  && make clean \
  && ldconfig \
  && cd / \
  && rm -rf /var/local/git/grpc
