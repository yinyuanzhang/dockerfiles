FROM golang:1.12 AS builder
WORKDIR /hojreh

COPY go.mod ./
RUN go mod download

COPY cmd cmd
COPY pkg pkg

RUN CGO_ENABLED=0 go build -o /go/bin/server -v ./cmd/server
RUN CGO_ENABLED=0 go build -o /go/bin/admin  -v ./cmd/admin

FROM alpine:3.9 AS final

COPY --from=builder /go/bin/server /bin/server
COPY --from=builder /go/bin/admin  /bin/admin

COPY .docker/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]