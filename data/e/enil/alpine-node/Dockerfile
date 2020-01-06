FROM alpine:3.4
MAINTAINER Emil Nilsson <eonilsson@gmail.com>

ARG TINI_VERSION=0.9.0-r1
ARG NODEJS_VERSION=6.2.0-r0

RUN apk update && apk add -u tini=${TINI_VERSION} nodejs=${NODEJS_VERSION}

ENTRYPOINT ["/sbin/tini", "-v", "--"]
CMD ["node", "-h"]

