FROM python:3.7-buster

# install packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential autoconf libtool pkg-config make automake g++ \
    ca-certificates netbase wget unzip git curl libgflags-dev libgtest-dev \
    zlib1g-dev clang libc++-dev libgfortran-7-dev \
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

# install python libs
RUN pip install -U pip \
  && pip install grpcio grpcio-tools numpy

COPY pip.conf /etc/pip.conf

# install golang
ENV GOLANG_VERSION=1.13
ENV GOROOT=/usr/local/go
ENV GOPATH=/go
ENV PATH="${PATH}:${GOROOT}/bin:${GOPATH}/bin"

RUN curl -O https://dl.google.com/go/go${GOLANG_VERSION}.linux-amd64.tar.gz \
  && tar -xf go${GOLANG_VERSION}.linux-amd64.tar.gz \
  && rm go${GOLANG_VERSION}.linux-amd64.tar.gz \
  && mv go /usr/local \
  && mkdir -p $GOPATH \
  && /usr/local/go/bin/go get -u github.com/golang/protobuf/protoc-gen-go
