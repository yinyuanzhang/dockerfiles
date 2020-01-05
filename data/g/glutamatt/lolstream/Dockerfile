FROM golang:1.11 AS builder
ADD https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 /usr/bin/dep
RUN chmod +x /usr/bin/dep

WORKDIR $GOPATH/src/github.com/username/repo
COPY Gopkg.toml Gopkg.lock ./
RUN dep ensure --vendor-only
COPY main.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -o /app .

FROM scratch
COPY --from=builder /app ./
COPY static ./static
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
ENTRYPOINT ["./app"]
