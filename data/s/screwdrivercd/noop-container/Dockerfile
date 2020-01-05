FROM alpine:latest
MAINTAINER Screwdriver <screwdriver.cd>

LABEL description="Minimal image to use in no-op operations in screwdriver"

# Based on https://github.com/screwdriver-cd/launcher/blob/master/Dockerfile
RUN set -x \
    # Alpine ships with musl instead of glibc (this fixes the symlink)
    # Ref https://docs.screwdriver.cd/user-guide/FAQ#how-do-i-fix-build-failed-to-start-error-message
    && mkdir /lib64 \
    && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
    # Need latest ca-certificates or post to https end-points can fail
    && apk add --no-cache --update ca-certificates \
    # Needed for sd-setup-screwdriver-sshca-bookend
    && apk add --no-cache curl openssh \
    # Need bash to support sd-cmd
    && apk add --no-cache bash
