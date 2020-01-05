# Multi-stage build setup (https://docs.docker.com/develop/develop-images/multistage-build/)

# Stage 1 (to create a "build" image, ~850MB)
FROM golang:latest AS go-builder
RUN go version

MAINTAINER Victor Jungbauer <victor.jungbauer@gmail.com>

COPY . /go/src/github.com/vic999/lox2lwz/
WORKDIR /go/src/github.com/vic999/lox2lwz/
RUN set -x && \
    go get -v

RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm GOARM=7 go build -a -o app .


# Stage 2 (to create a downsized "container executable", ~7MB)

# If you need SSL certificates for HTTPS, replace `FROM SCRATCH` with:
#
FROM alpine:3.7
RUN apk --no-cache add ca-certificates
#
#FROM scratch
WORKDIR /root/
COPY --from=go-builder /go/src/github.com/vic999/lox2lwz/app .

EXPOSE 8002
CMD ["./app"]
