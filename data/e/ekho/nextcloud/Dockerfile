# DO NOT EDIT: created by update.sh from Dockerfile-alpine.template
FROM alpine:3.8

RUN set -ex; \
    \
    apk add --no-cache \
        autoconf \
        automake \
        make \
        git \
        g++ \
        fuse \
        fuse-dev \
        libcurl \
        curl-dev \
        libxml2 \
        libxml2-dev

RUN set -ex; \
    \
    git clone https://github.com/s3fs-fuse/s3fs-fuse.git

RUN set -ex; \
    \
    cd s3fs-fuse; \
    ./autogen.sh; \
    ./configure --disable-dependency-tracking; \
    make

FROM nextcloud:fpm-alpine

RUN set -ex; \
    \
    apk add --no-cache \
        fuse \
        libcurl \
        libxml2

COPY --from=0 /s3fs-fuse/src/s3fs /usr/local/bin/

COPY *.sh /
ENTRYPOINT ["/entrypoint-custom.sh"]