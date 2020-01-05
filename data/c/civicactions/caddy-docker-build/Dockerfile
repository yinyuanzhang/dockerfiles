#
# Build stage
#
FROM golang:1.12-alpine AS builder

# System dependencies
RUN apk add --no-cache git gcc musl-dev

# Go modules
ENV GO111MODULE=on
WORKDIR /caddy
COPY go.* /caddy/
RUN go mod download && go mod verify

# Caddy code
COPY *.go /caddy/
RUN CGO_ENABLED=0 go build -o /go/bin/caddy

# Process wrapper
RUN go get -v github.com/abiosoft/parent

#
# Final stage
#
FROM alpine:3.10

# System dependencies
RUN apk add --no-cache \
    ca-certificates \
    mailcap \
    tzdata \
    && update-ca-certificates

# Install caddy
COPY --from=builder /go/bin/caddy /usr/bin/caddy

# Install process wrapper
COPY --from=builder /go/bin/parent /bin/parent

# Validate install
RUN /usr/bin/caddy -version && /usr/bin/caddy -plugins

EXPOSE 80 443 2015
VOLUME /root/.caddy /srv
WORKDIR /srv

ENTRYPOINT ["/bin/parent", "caddy"]
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree=true"]
