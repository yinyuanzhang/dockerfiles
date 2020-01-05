FROM php:fpm-alpine

ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG PECL_GRPC_VERSION="1.22.0"
ARG PROTOC_VERSION="3.9.0"
ARG PROTOC_DOWNLOAD_FILE="protoc-${PROTOC_VERSION}-linux-x86_64.zip"
ARG PROTOC_URL="https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip"

RUN set -x \
    && apk update \
    && apk add --no-cache \
        gcc \
    && apk add --no-cache --virtual needless_libset \
        autoconf \
        automake \
        curl \
        g++ \
        git \
        libtool \
        make \
        zlib-dev \
    && cd /tmp \
    && if [ "x" != "x${HTTPS_PROXY}" ]; then \
        curl -x ${HTTPS_PROXY} -L -o ${PROTOC_DOWNLOAD_FILE} ${PROTOC_URL}; \
    else \
        curl -L -o ${PROTOC_DOWNLOAD_FILE} ${PROTOC_URL}; \
    fi \
    && unzip ${PROTOC_DOWNLOAD_FILE} \
    && mv include/google /usr/include \
    && git clone -b "v${PECL_GRPC_VERSION}" https://github.com/grpc/grpc \
    && cd grpc \
    && git submodule update --init \
    && make grpc_php_plugin \
    && mv bins/opt/protobuf/protoc /usr/bin/protoc \
    && mv bins/opt/grpc_php_plugin /usr/lib/grpc_php_plugin \
    && if [ "x" != "x${HTTP_PROXY}" ]; then \
        pear config-set http_proxy ${HTTP_PROXY}; \
    fi \
    && pecl install "grpc-${PECL_GRPC_VERSION}" "protobuf-${PROTOC_VERSION}" \
    && apk del needless_libset \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*

COPY ./compile.sh ./

CMD ["sh", "compile.sh"]
