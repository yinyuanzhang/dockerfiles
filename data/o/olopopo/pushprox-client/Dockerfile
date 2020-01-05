FROM golang:alpine AS build

RUN apk update &&  \
    apk upgrade && \
    apk add --no-cache git && \
    go get github.com/stratio/pushprox/client && \
    cd /go/src/github.com/stratio/pushprox/client && \
    go build

FROM alpine
MAINTAINER Marcos Lorenzo de Santiago <marcos.lorenzodesantiago@gmail.com>
LABEL Description="ProxPush client docker image"
COPY --from=build /go/bin/client /pushprox-client

ENTRYPOINT [ "/pushprox-client" ]
