FROM golang:alpine as gobuild

RUN apk update && apk add build-base gcc git && go get -v github.com/cloudflare/cloudflared/cmd/cloudflared

WORKDIR /go/src/github.com/cloudflare/cloudflared/cmd/cloudflared

RUN go build ./


FROM alpine:latest

ENV PORT 53
ENV DNS1 1.1.1.1
ENV DNS2 1.0.0.1

EXPOSE $PORT/tcp $PORT/udp

RUN apk add bind-tools ca-certificates

COPY --from=gobuild /go/src/github.com/cloudflare/cloudflared/cmd/cloudflared/cloudflared /usr/local/bin/cloudflared

HEALTHCHECK --interval=5s --timeout=3s --start-period=5s CMD nslookup -po=${PORT} cloudflare.com 127.0.0.1 || exit 1
CMD ["/bin/sh", "-c", "/usr/local/bin/cloudflared proxy-dns --address 0.0.0.0 --port ${PORT} --upstream https://${DNS1}/dns-query --upstream https://${DNS2}/dns-query"]

LABEL maintainer="Marco Kundt"
