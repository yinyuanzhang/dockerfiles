# Pull in qemu-arm-static for cross-compiling
# See https://github.com/multiarch/qemu-user-static/issues/37 for background.
FROM multiarch/qemu-user-static:x86_64-arm as qemu
MAINTAINER Richard Alimi <rich@velvetsea.net>
FROM alpine as qemu_extract
COPY --from=qemu /usr/bin qemu_user_static.tgz
RUN tar -xzvf qemu_user_static.tgz

# Setup image used for building.
FROM arm32v6/golang:alpine as builder
COPY --from=qemu_extract qemu-* /usr/bin
RUN apk add --no-cache gcc git make musl-dev

# Setup build directory and build.
WORKDIR /go/src/github.com/prometheus/node_exporter
RUN git clone --branch=v0.16.0 --depth=1 https://github.com/prometheus/node_exporter.git .
RUN GOOS=linux GOARCH=arm make build

# Create minimal image with built binary
FROM arm32v6/alpine
COPY --from=builder /go/src/github.com/prometheus/node_exporter/node_exporter /
EXPOSE 9100/tcp
ENTRYPOINT [ "/node_exporter" ]
