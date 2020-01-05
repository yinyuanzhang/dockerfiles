# Build
FROM golang:alpine as builder
RUN apk add -U --no-cache ca-certificates git
RUN mkdir /build
ADD . /build/
WORKDIR /build
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -a -ldflags="-w -s"


# Dockerize
FROM scratch
MAINTAINER seekie <seekie.xyz@gmail.com>

ENV PROXY_SERVER_CONFIG "/config.json"

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /build/simple-proxy-server /
COPY --from=builder /build/config.json /

VOLUME ["/certs"]

CMD ["/simple-proxy-server"]
