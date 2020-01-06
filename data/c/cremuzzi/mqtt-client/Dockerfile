FROM golang:1.11.2-alpine3.8 AS builder

RUN apk add --no-cache --virtual .build-deps \
       git \
       upx \
    && go get -v github.com/eclipse/paho.mqtt.golang \
    && go install -v -ldflags "-s -w" github.com/eclipse/paho.mqtt.golang/cmd/sample \
    && upx --brute /go/bin/sample \
    && apk del .build-deps

FROM alpine:3.8

LABEL maintainer="Carlos Remuzzi <carlosremuzzi@gmail.com>"

COPY --from=builder /go/bin/sample /usr/local/bin/mqtt

CMD ["mqtt"]
