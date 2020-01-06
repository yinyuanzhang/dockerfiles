ARG GRPC_BUILD_PYTHON_VERSION=latest

FROM raisepartner/grpc-build-python:${GRPC_BUILD_PYTHON_VERSION}

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
