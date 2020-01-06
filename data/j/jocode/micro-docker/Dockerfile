FROM golang:alpine
ARG GOLANGCI_LINT_VERSION=1.16.0
RUN adduser -u 1000 -D jenkins && \
  wget -O - -q https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh \
  | ash -s v$GOLANGCI_LINT_VERSION && \
  apk add --no-cache make git gcc protobuf musl-dev && \
  go get -v -u github.com/micro/micro && \
  go get -v -u github.com/micro/go-micro && \
  go get -v -u github.com/micro/protoc-gen-micro && \
  go get -v -u github.com/golang/protobuf/proto && \
  go get -v -u github.com/golang/protobuf/protoc-gen-go && \
  mkdir /.cache && chmod -R 777 /.cache $GOPATH
