FROM golang:latest

RUN go get github.com/kyoh86/scopelint && \
    go get -u github.com/jstemmer/go-junit-report && \
    go get -u github.com/golangci/golangci-lint/cmd/golangci-lint

ENV GO111MODULE on
