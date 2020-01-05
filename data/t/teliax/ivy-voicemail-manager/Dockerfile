FROM golang:alpine as builder
RUN mkdir -p /go/src/github.com/teliax/ivy-voicemail-manager
ADD . /go/src/github.com/teliax/ivy-voicemail-manager/
WORKDIR /go/src/github.com/teliax/ivy-voicemail-manager 
RUN apk add git
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep ensure
RUN go build -o ivy-voicemail-manager .
FROM alpine
MAINTAINER Teliax <developers@teliax.com>
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
RUN update-ca-certificates
COPY --from=builder /go/src/github.com/teliax/ivy-voicemail-manager/ivy-voicemail-manager /opt/ivy-voicemail-manager/
WORKDIR /opt/ivy-voicemail-manager
CMD ["./ivy-voicemail-manager"]
