FROM golang:alpine
ARG GOLANGCI_LINT_VERSION=1.22.2
RUN adduser -u 1000 -D jenkins && \
  wget -O - -q https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh \
  | ash -s v$GOLANGCI_LINT_VERSION && \
  apk add --no-cache make git gcc g++ protobuf && \
  go get -u github.com/golang/protobuf/protoc-gen-go && \
  go get github.com/micro/protoc-gen-micro && \
  mkdir /.cache && chmod -R 777 /.cache $GOPATH
