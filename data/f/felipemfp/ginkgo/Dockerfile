FROM golang:1.10.3-alpine

RUN apk add git make

RUN go get -u github.com/onsi/ginkgo/ginkgo

ENTRYPOINT ginkgo
