# Build stage
FROM golang:latest

ENV GOBIN /go/bin

WORKDIR ~ 

RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz && \
tar xzf protobuf-all-3.6.1.tar.gz && \
cd protobuf-3.6.1 && \
apt-get update && \
apt-get install -y build-essential autoconf automake libtool curl make g++ unzip && \
./configure && \
make && \
make check && \
make install && \
ldconfig && \
protoc --version 

RUN go get -u github.com/golang/dep/cmd/dep
#instal grpc e protobuf
RUN go get -u google.golang.org/grpc
RUN go get -u github.com/golang/protobuf/protoc-gen-go
