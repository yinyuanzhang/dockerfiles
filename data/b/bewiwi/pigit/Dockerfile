FROM golang:1.13-stretch AS build-env

ARG version

COPY ./ /go/src/gitlhub.com/bewiwi/pigit
WORKDIR /go/src/gitlhub.com/bewiwi/pigit

RUN go build -o /go/bin/pigit main.go

# Final stage
FROM debian:stable

RUN apt-get update
RUN apt-get install -y ca-certificates

RUN useradd pigit
WORKDIR /app
COPY --from=build-env /go/bin/pigit /app/
USER pigit

ENTRYPOINT ["/app/pigit", "--config", "/app/config.yml"]