FROM alpine:latest

RUN apk update && \
	apk add --update curl && \
	rm -rf /var/cache/apk/*
ENTRYPOINT ["/usr/bin/curl"]


