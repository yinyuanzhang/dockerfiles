FROM golang:alpine

RUN apk update \
  && apk add --virtual build-dependencies git \
  && apk add bash curl jq \
  && go get -u github.com/fullstorydev/grpcurl \
  && go install github.com/fullstorydev/grpcurl/cmd/grpcurl \
  && rm -rf /go/pkg \
  && rm -rf /go/src \
  && apk del build-dependencies \
  && rm -rf /var/cache/apk/*
