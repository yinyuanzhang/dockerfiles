FROM golang:1.13.4 as golang

WORKDIR /bcloud-build

COPY go.mod go.mod
COPY go.sum go.sum
RUN go mod download

COPY gen gen
COPY pkg pkg
COPY main.go main.go
RUN CGO_ENABLED=0 GOOS=linux go build -o /bcloud-agent -mod=readonly .


FROM debian:stretch-20190204-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        dnsutils \
        iptables \
        jq \
        nghttp2 \
        procps \
    && rm -rf /var/lib/apt/lists/*

COPY --from=golang /bcloud-agent .
ENTRYPOINT ["./bcloud-agent"]
