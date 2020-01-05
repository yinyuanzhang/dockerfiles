FROM golang:1.9.2-alpine3.6 AS build-env

RUN apk --no-cache add gcc musl-dev git
RUN go get github.com/rubenv/sql-migrate/sql-migrate

FROM alpine:3.6

COPY --from=build-env /go/bin/sql-migrate /bin

RUN apk --no-cache add bash mysql-client
