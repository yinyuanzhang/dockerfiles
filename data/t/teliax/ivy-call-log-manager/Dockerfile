FROM golang:alpine as builder
RUN mkdir -p /go/src/github.com/teliax/ivy-call-log-manager
ADD . /go/src/github.com/teliax/ivy-call-log-manager/
WORKDIR /go/src/github.com/teliax/ivy-call-log-manager
RUN apk add git
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep ensure
RUN go build -o ivy-call-log-manager .
FROM alpine
MAINTAINER Teliax <developers@teliax.com>
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
RUN update-ca-certificates
COPY --from=builder /go/src/github.com/teliax/ivy-call-log-manager/ivy-call-log-manager /opt/ivy-call-log-manager/
WORKDIR /opt/ivy-call-log-manager
CMD ["./ivy-call-log-manager"]
