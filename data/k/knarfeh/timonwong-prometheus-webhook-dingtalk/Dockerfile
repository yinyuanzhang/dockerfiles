FROM golang:alpine as builder
LABEL maintainer="hejun@megvii.com"

RUN apk --no-cache add curl git make perl
RUN curl -s https://glide.sh/get | sh
COPY . /go/src/github.com/timonwong/prometheus-webhook-dingtalk
RUN cd /go/src/github.com/timonwong/prometheus-webhook-dingtalk && make build


FROM alpine:3.4
EXPOSE 8086
RUN apk add --update ca-certificates
COPY --from=builder /go/src/github.com/timonwong/prometheus-webhook-dingtalk/prometheus-webhook-dingtalk /usr/local/bin/prometheus-webhook-dingtalk

ENTRYPOINT [ "prometheus-webhook-dingtalk" ]
