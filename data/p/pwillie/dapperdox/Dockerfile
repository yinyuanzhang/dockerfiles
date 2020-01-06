FROM golang:1.10 AS build-stage

WORKDIR /go/src/github.com/dapperdox/dapperdox
COPY . .

RUN go build -v -ldflags '-w -linkmode external -extldflags "-static"' -o dapperdox .

# Final Stage
FROM alpine:3.7

# RUN apk add -U -q --no-progress ca-certificates

COPY --from=build-stage /go/src/github.com/dapperdox/dapperdox/dapperdox /bin/
COPY --from=build-stage /go/src/github.com/dapperdox/dapperdox/assets    /opt/assets/
RUN chmod +x /bin/dapperdox

WORKDIR /dapperdox

ENTRYPOINT [ \
  "dapperdox", \
  "-assets-dir", "/dapperdox/assets", \
  "-bind-addr", "0.0.0.0:8080", \
  "-default-assets-dir", "/opt/assets", \
  "-spec-dir", "/dapperdox/specifications" \
]
