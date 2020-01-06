FROM golang:1.9-alpine as builder
RUN apk add --no-cache make gcc musl-dev linux-headers git

RUN git clone https://github.com/ethereum/go-ethereum.git --depth 1 /go-ethereum \
    && cd /go-ethereum \
    && make all

FROM alpine:latest
COPY --from=builder /go-ethereum/build/bin/bootnode /usr/local/bin/

ENV NODE_KEY ''

EXPOSE 30301
CMD /bin/sh -c 'bootnode --nodekeyhex=$NODE_KEY'
