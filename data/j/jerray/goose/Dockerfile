FROM alpine:latest

ENV GOOSE_URL=https://github.com/pressly/goose/releases/download/v2.7.0-rc3/goose-linux64

RUN apk add --update --no-cache ca-certificates curl \
    && curl -L -o /bin/goose $GOOSE_URL \
    && chmod 0755 /bin/goose
