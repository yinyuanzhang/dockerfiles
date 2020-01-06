FROM alpine:3.8

ENV LANG=C.UTF-8 \
    GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc \
    GLIBC_VERSION=2.28-r0

RUN set -eux && \
    apk upgrade -U && \
    wget -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    for pkg in glibc glibc-bin glibc-i18n; \
    do \
        wget -P /tmp ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}-${GLIBC_VERSION}.apk; \
    done && \
    apk add /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef -c -i POSIX -f UTF-8 ${LANG} || true ) && \
    echo "export LANG=${LANG}" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    apk del glibc-i18n && \
    rm -rf /var/cache/apk/* /etc/apk/keys/sgerrand.rsa.pub /tmp/*.apk && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
