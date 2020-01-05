FROM alpine:3.6

RUN GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" && \
    GLIBC_PACKAGE_VERSION="2.25-r0" && \
    GLIBC_PACKAGE_FILENAME="glibc-$GLIBC_PACKAGE_VERSION.apk" && \
    apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    wget \
        "https://raw.githubusercontent.com/andyshinn/alpine-pkg-glibc/master/sgerrand.rsa.pub" \
        -O "/etc/apk/keys/sgerrand.rsa.pub" && \
    wget \
        "$GLIBC_BASE_URL/$GLIBC_PACKAGE_VERSION/$GLIBC_PACKAGE_FILENAME" && \
    apk add --no-cache \
        "$GLIBC_PACKAGE_FILENAME" && \
    \
    rm "/etc/apk/keys/sgerrand.rsa.pub" && \
    /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    \
    rm "/root/.wget-hsts" && \
    apk del .build-dependencies && \
    rm \
        "$GLIBC_PACKAGE_FILENAME"

ENV LANG=C.UTF-8
