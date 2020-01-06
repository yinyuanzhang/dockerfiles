FROM golang:1.11 as builder
COPY . /go/src/github.com/away-team/migrate
WORKDIR /go/src/github.com/away-team/migrate
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags "-s" -installsuffix cgo -o bin/migrate *.go

FROM alpine:latest

RUN apk update && \
    apk add ca-certificates bash && \
    rm -rf /var/cache/apk/*

WORKDIR /
COPY --from=builder /go/src/github.com/away-team/migrate/bin/migrate .
ENTRYPOINT ["/migrate"]
