FROM golang:1.10-alpine3.8 AS build

RUN apk add --no-cache git \
	&& go get -u github.com/rakyll/hey


FROM alpine:3.8

COPY --from=build /go/bin/hey /usr/local/bin/hey

ENTRYPOINT ["hey"]
