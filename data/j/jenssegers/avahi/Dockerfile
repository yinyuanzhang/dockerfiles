FROM alpine:edge

ARG AVAHI_VERSION=0.7
ARG AVAHI_RELEASE=r1

RUN apk add --no-cache \
    avahi=$AVAHI_VERSION-$AVAHI_RELEASE \
    avahi-tools=$AVAHI_VERSION-$AVAHI_RELEASE

ENTRYPOINT ["avahi-daemon"]
