FROM golang:1.12 as builder
#test
ENV GOOS=linux
ENV GOARCH=amd64
ENV CGO_ENABLED=0

COPY src/ /go/src/vault-secret-styx/

RUN cd /go/src/vault-secret-styx/ && go get && go build

FROM alpine

COPY --from=builder /go/src/vault-secret-styx/vault-secret-styx /

RUN chmod +x vault-secret-styx

ENTRYPOINT ["/vault-secret-styx"]
