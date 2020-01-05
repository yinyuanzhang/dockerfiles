FROM golang:1.10-alpine as builder

RUN apk update && apk add git make gcc libc-dev

RUN go get github.com/coreos/dex

RUN cd /go/src/github.com/coreos/dex && make release-binary

FROM alpine:latest

COPY --from=builder /go/bin/dex /usr/bin/dex
COPY --from=builder /go/src/github.com/coreos/dex/web /web

RUN apk update && apk add ca-certificates

ENTRYPOINT ["/usr/bin/dex"]
