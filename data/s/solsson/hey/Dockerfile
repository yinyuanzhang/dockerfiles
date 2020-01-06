FROM golang:1.12.5-alpine3.9@sha256:06ba1dae97f2bf560831497f8d459c68ab75cc67bf6fc95d9bd468ac259c9924 AS builder

COPY . /go/src/github.com/rakyll/hey

RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \
  go install -ldflags '-w -extldflags "-static"' \
  /go/src/github.com/rakyll/hey

FROM scratch

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/bin/hey /hey

ENV PORT 8080
EXPOSE $PORT

ENTRYPOINT ["/hey"]
