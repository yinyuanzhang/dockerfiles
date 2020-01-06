FROM golang:alpine
ARG GOLANGCI_LINT_VERSION=1.16.0
RUN wget -O - -q https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh \
  | ash -s v$GOLANGCI_LINT_VERSION && \
  apk add --no-cache make git gcc protobuf musl-dev 
RUN go get github.com/golang/protobuf/proto && \
  go get github.com/golang/protobuf/protoc-gen-go && \
  go get github.com/micro/protoc-gen-micro && \
  go get github.com/micro/go-micro && \
  go get github.com/micro/micro
RUN adduser -u 1000 -D jenkins && \
  mkdir -p /home/jenkins/.cache && chmod -R 777 /home/jenkins/.cache && \
  mkdir -p /go/pkg/mod/cache && chmod -R 777 /go $GOPATH 