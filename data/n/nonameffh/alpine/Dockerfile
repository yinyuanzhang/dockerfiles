FROM alpine:latest

LABEL maintainer="Aleksey Tarasov <nonameffh@gmail.com>"

ENV INSTALLED_PACKAGES \
    autoconf \
    dpkg-dev dpkg \
    file \
    g++ \
    gcc \
    libc-dev \
    make \
    nano \
    pkgconf \
    re2c \
    ca-certificates \
    curl \
    tar \
    xz \
    wget \
    gnupg \
    openssl \
    su-exec \
    bash \
    net-tools \
    coreutils \
    shadow


RUN apk add --no-cache --virtual .base_deps $INSTALLED_PACKAGES

CMD ["bash"]