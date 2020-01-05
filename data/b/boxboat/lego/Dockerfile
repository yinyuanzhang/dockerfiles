FROM golang:alpine3.8 AS build

RUN apk add --no-cache \
		curl \
		git \
		make

RUN mkdir -p /go/src/github.com/xenolf \
	&& cd /go/src/github.com/xenolf \
	&& git clone -b "v2.2.0" --single-branch --depth 1 "https://github.com/xenolf/lego.git" \
	&& cd lego \
	&& env GOOS=linux GOARCH=amd64 CGO_ENABLED=0 make build

FROM alpine:3.8

RUN apk add --no-cache \
		ca-certificates

COPY --from=build /go/src/github.com/xenolf/lego/dist/lego /usr/local/bin/lego

RUN addgroup -g 1000 alpine && \
    adduser -u 1000 -G alpine -h /home/alpine -s /bin/sh -D alpine

WORKDIR /home/alpine
USER alpine:alpine
ENTRYPOINT [ "/usr/local/bin/lego" ]
