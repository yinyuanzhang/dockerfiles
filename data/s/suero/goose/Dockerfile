FROM golang:alpine as builder

LABEL version="1.0"
LABEL maintainer="suerorenato@gmail.com"

WORKDIR /go/src/github.com/pressly
RUN apk update && apk add git gcc libc-dev && \
		git clone https://github.com/renatosuero/goose.git && \
		cd goose/cmd/goose && go get && go install && \
		rm -rf /var/cache/apk/*

FROM alpine:latest 

LABEL version="1.0"
LABEL maintainer="suerorenato@gmail.com"

WORKDIR /bin/migrations
COPY --from=builder /go/bin/ /bin
