FROM golang:alpine as builder
MAINTAINER Richard Alimi <rich@velvetsea.net>

# Add packages necessary to build
RUN apk add --no-cache \
    git \
    make

# Setup the build directory
WORKDIR /go/src/github.com/prometheus/prometheus
RUN git clone --branch=v2.3.2 --depth=1 https://github.com/prometheus/prometheus.git .

# Build the binary for ARM
RUN GOOS=linux GOARCH=arm make build

# Create minimal image with built binary
FROM alpine:latest
COPY --from=builder /go/src/github.com/prometheus/prometheus/prometheus /
EXPOSE 9090/tcp
ENTRYPOINT [ "/prometheus" ]
