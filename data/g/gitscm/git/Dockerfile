#
# Copyright (C) 2019 Olliver Schinagl <oliver@schinagl.nl>
#
# SPDX-License-Identifier: GPL-2.0-or-later

# For Alpine, latest is actually the latest stable
# hadolint ignore=DL3007
FROM registry.hub.docker.com/library/alpine:latest AS builder

LABEL Maintainer="Olliver Schinagl <oliver@schinagl.nl>"

WORKDIR /build

# We want the latest stable version from the repo
# hadolint ignore=DL3018
RUN \
    apk add --no-cache \
        asciidoc \
        build-base \
        curl-dev \
        expat-dev \
        libressl-dev \
        pcre2-dev \
        perl-dev \
        perl-error \
        python2-dev \
        xmlto \
        zlib-dev \
    && \
    rm -rf "/var/cache/apk/"*

COPY . "/build"
COPY "./contrib/docker/config.mak" "/build"

RUN \
    make prefix="/usr" && \
    make prefix="/usr" DESTDIR="/alpine/" install

# For Alpine, latest is actually the latest stable
# hadolint ignore=DL3007
FROM registry.hub.docker.com/library/alpine:latest

RUN \
    apk add --no-cache \
        git-daemon \
	gnupg \
    && \
    rm -rf "/var/cache/apk/"* && \
    for gitfile in $(apk info -L git); do \
        if [ -f "/${gitfile}" ]; then \
            rm "/${gitfile:?}"; \
        fi \
    done

COPY --from=builder "/alpine/" "/"

COPY "contrib/docker/docker-entrypoint.sh" "/init"

ENTRYPOINT [ "/init" ]
