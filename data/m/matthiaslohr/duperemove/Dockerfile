
FROM alpine:edge
LABEL maintainer="Matthias Lohr <mail@mlohr.com>"

RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing duperemove

ENTRYPOINT ["/usr/sbin/duperemove"]

