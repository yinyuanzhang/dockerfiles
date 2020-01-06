FROM alpine:latest

ENV GOPATH /go

RUN apk add --no-cache ca-certificates \
&& apk add --no-cache --virtual .build-deps build-base git go \
&& go get bitbucket.org/liamstask/goose/cmd/goose \
&& cp -pr /go/bin/goose /usr/bin \
&& rm -rf /go \
&& apk del .build-deps \
&& mkdir /db

ENTRYPOINT ["/usr/bin/goose"]
