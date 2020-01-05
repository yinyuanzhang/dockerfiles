FROM golang:1.11.1-alpine3.8
LABEL maintainer "nownabe <nownabe@gmail.com>"

ENV golangci_lint_version 1.11.2

ENV GO111MODULE=on

RUN \
  apk --update --no-cache add \
    bash \
    gcc \
    git \
    musl-dev \
  && wget -O - -q https://install.goreleaser.com/github.com/golangci/golangci-lint.sh \
    | sh -s v${golangci_lint_version}
