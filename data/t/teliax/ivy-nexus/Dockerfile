FROM golang:alpine as builder
RUN mkdir -p /go/src/github.com/teliax/ivy-nexus
ADD . /go/src/github.com/teliax/ivy-nexus/
WORKDIR /go/src/github.com/teliax/ivy-nexus 
RUN apk add git
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep ensure
RUN go build -o ivy-nexus .
FROM alpine
MAINTAINER Teliax <developers@teliax.com>
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
RUN update-ca-certificates
COPY --from=builder /go/src/github.com/teliax/ivy-nexus/ivy-nexus /opt/ivy-nexus/
WORKDIR /opt/ivy-nexus
CMD ["./ivy-nexus"]