FROM debian:stretch-slim
LABEL maintainer "nownabe"


ARG protoc_version=3.6.1
ARG go_version=1.11.4
ARG go_sha256=fb26c30e6a04ad937bbc657a1b5bba92f80096af1e8ee6da6430c045a8db3a5b
ARG grpc_web_version=1.0.3


ENV DEBIAN_FRONTEND noninteractive
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH


ENV build_deps \
  ca-certificates \
  curl \
  git \
  unzip
ENV runtime_deps \
  make


RUN apt-get update \
  && apt-get install -y --no-install-recommends ${build_deps} \
  && apt-get install -y --no-install-recommends ${runtime_deps} \
  && : ================ Install protoc ================ \
  && curl -SsLO https://github.com/protocolbuffers/protobuf/releases/download/v${protoc_version}/protoc-${protoc_version}-linux-x86_64.zip \
  && unzip -d /usr/local protoc-${protoc_version}-linux-x86_64.zip \
  && rm -f /usr/local/readme.txt protoc-${protoc_version}-linux-x86_x64.zip \
  && : ================ Install go ================ \
  && curl -SsLO https://golang.org/dl/go${go_version}.linux-amd64.tar.gz \
  && echo "${go_sha256} go${go_version}.linux-amd64.tar.gz" | sha256sum -c - \
  && tar xf go${go_version}.linux-amd64.tar.gz -C /usr/local \
  && mkdir -p $GOPATH/src GOPATH/bin \
  && go get -u google.golang.org/grpc \
  && go get -u github.com/golang/protobuf/protoc-gen-go \
  && : ================ Install gRPC-web ================ \
  && curl -SsL -o /usr/local/bin/protoc-gen-grpc-web https://github.com/grpc/grpc-web/releases/download/${grpc_web_version}/protoc-gen-grpc-web-${grpc_web_version}-linux-x86_64 \
  && chmod +x /usr/local/bin/protoc-gen-grpc-web \
  && : ================ Clean up ================ \
  && apt-get remove -y ${build_deps} \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
