# build executable binary
FROM golang:alpine AS builder

# Install git, gcc and other dependencies.
RUN apk update && apk add --no-cache --virtual .build-deps \
      alpine-sdk \
      cmake \
      sudo \
      libssh2 libssh2-dev\
      git

WORKDIR ~/app/
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN make install

# build smallest image
FROM alpine
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY --from=builder /go/bin/fluxmonitor /usr/local/bin/fluxmonitor
ENTRYPOINT ["fluxmonitor"]
