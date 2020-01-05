FROM golang:1.10-alpine as build
COPY . /go/src/github.com/magnaz/concourse-telegram-resource
WORKDIR /go/src/github.com/magnaz/concourse-telegram-resource
RUN set -ex && \
    apk add --no-cache git && \
    go get && \
    go build -o /go/bin/telegram

FROM alpine:3.7
COPY --from=build /go/bin/telegram /opt/resource/telegram
RUN set -ex && \
    apk add --no-cache ca-certificates && \
    ln -s /opt/resource/telegram /opt/resource/check && \
    ln -s /opt/resource/telegram /opt/resource/in && \
    ln -s /opt/resource/telegram /opt/resource/out
