FROM golang:alpine as builder
RUN apk add --no-cache git gcc musl-dev
RUN go get github.com/pressly/goose/cmd/goose

FROM alpine:latest
ENV DRIVER=postgres
ENV CONNECTION_STRING="user=user dbname=db password=password host=db port=5432 sslmode=disable"
ENV COMMAND=up
WORKDIR /app
RUN mkdir /app/data
VOLUME /app/data
COPY --from=builder /go/bin/goose .
CMD ["/bin/sh", "-c", "/app/goose -dir /app/data ${DRIVER} \"${CONNECTION_STRING}\" ${COMMAND}"]
