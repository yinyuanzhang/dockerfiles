FROM golang:alpine as build
ENV RELEASE_TAG 2.0.33
RUN apk --no-cache add git && \
    git clone https://github.com/DNSCrypt/dnscrypt-proxy /go/src/github.com/DNSCrypt/ && \
    cd /go/src/github.com/DNSCrypt/dnscrypt-proxy && \
    git checkout tags/${RELEASE_TAG} && \
    CGO_ENABLED=0 GOOS=linux go install -a -ldflags '-s -w -extldflags "-static"' -v ./...

FROM alpine
RUN apk --no-cache add ca-certificates
COPY --from=build /go/bin/dnscrypt-proxy /usr/local/bin/dnscrypt-proxy
ADD config /config
RUN mkdir /blacklist/ ; touch /blacklist/blacklist.txt
EXPOSE 53/udp

CMD ["dnscrypt-proxy", "-config", "/config/dnscrypt-proxy.toml"]
