FROM golang:alpine3.8
MAINTAINER Ali Al-Shabibi <alshabibi.ali@gmail.com>

RUN apk update && apk add git gcc musl-dev

RUN go get -u github.com/onsi/ginkgo/ginkgo && go get -u github.com/onsi/gomega/...

WORKDIR /go/src

COPY go-entrypoint ./go-entrypoint
RUN chmod +x go-entrypoint
ENTRYPOINT ["./go-entrypoint"]
