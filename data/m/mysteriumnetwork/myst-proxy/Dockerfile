FROM golang:1.13-alpine AS builder

# Install packages
RUN apk add --update --no-cache git

# Install application
WORKDIR /go/src/github.com/mysteriumnetwork/supernode
ADD . .

# Build application
RUN go run ci/mage.go buildConsumerProxy

FROM mysteriumnetwork/myst:0.16.2-alpine

RUN apk add --update --no-cache ca-certificates \
    && update-ca-certificates 2>/dev/null || true

COPY --from=builder /go/src/github.com/mysteriumnetwork/supernode/build/consumerproxy /consumerproxy

ADD docker/consumer/consumer-proxy.sh consumer-proxy.sh

EXPOSE 8888 4050

ENTRYPOINT ["./consumer-proxy.sh"]
