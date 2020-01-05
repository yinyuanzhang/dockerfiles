FROM golang:1.12-alpine

#install Glide
RUN apk add --no-cache git curl openssh openssl tar gzip bash ca-certificates && \
    curl https://glide.sh/get | sh

RUN go get -u github.com/golang/dep/cmd/dep
