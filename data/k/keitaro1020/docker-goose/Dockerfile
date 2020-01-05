FROM golang:1.9-alpine
MAINTAINER keitaro1020

RUN apk add --update git g++ \
  && rm -rf /var/cache/apk/*


RUN go get bitbucket.org/liamstask/goose/cmd/goose

RUN mkdir /db
WORKDIR /

VOLUME ["/db"]

ENTRYPOINT ["/go/bin/goose"]
CMD ["status"]
