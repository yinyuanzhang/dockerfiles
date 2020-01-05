FROM alpine:3.8
#based on https://raw.githubusercontent.com/vgist/dockerfiles/master/smartmontools/Dockerfile

RUN set -xe && \
    apk add --no-cache \
    smartmontools python

ENTRYPOINT ["/usr/sbin/smartd", "--debug"]