FROM golang:1.10-alpine
MAINTAINER dyoshikawa

RUN apk add -U --no-cache git

RUN mkdir /go/src/app
WORKDIR /go/src/app
COPY main.go .

RUN go get -u github.com/codegangsta/gin
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep init
RUN dep ensure

CMD gin
