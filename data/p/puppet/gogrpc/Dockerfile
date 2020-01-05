FROM golang:latest as builder
RUN apt update && apt install unzip
RUN go get github.com/githubnemo/CompileDaemon && cp /go/bin/CompileDaemon /CompileDaemon
COPY --from=gcr.io/puppet-discovery/vault-client-alpine:latest /vault_client_bin /vault_client
COPY ./buildit.sh /tmp
WORKDIR /go

RUN cd /tmp && ./buildit.sh && rm ./buildit.sh
