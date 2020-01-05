FROM golang:stretch AS builder

RUN go get -d github.com/Keleir/httpd_exporter && \
    cd $GOPATH/src/github.com/Keleir/httpd_exporter && \
    CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /app

# Multistage
FROM scratch
COPY --from=builder /app /app

ENTRYPOINT ["/app"]
