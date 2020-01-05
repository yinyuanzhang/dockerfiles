FROM golang:1.11-alpine

RUN apk add --update --no-cache \
    autoconf \
    automake \
    curl \
    gcc \
    git \
    g++ \
    libgcc \
    libtool \
    libstdc++ \
    make \
    musl \
    unzip \
    zlib

# install kitgen
RUN go get -u github.com/nyarly/inlinefiles \
 && go get -u github.com/go-kit/kit/cmd/kitgen

# install protobuf
RUN curl -sSL -o /tmp/protobuf.zip https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-cpp-3.6.1.zip \
 && unzip /tmp/protobuf.zip -d /tmp/ \
 && cd /tmp/protobuf-3.6.1 \
 && ./configure --prefix=/usr \
 && make \
 && make install \
 && cd /go \
 && rm -rf /tmp/protobuf*
