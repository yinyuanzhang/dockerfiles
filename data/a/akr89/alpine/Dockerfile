FROM alpine:3.9 AS builder

# Install gosu (https://github.com/tianon/gosu)
# Add entrypoint script
ARG GOSU_VERSION=1.11
ARG GOSU_ARCH=amd64
ADD https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${GOSU_ARCH} \
    ./entrypoint.sh \
    /opt/
RUN mv /opt/gosu-${GOSU_ARCH} /opt/gosu && \
    chmod a+x /opt/gosu && \
    chmod a+x /opt/entrypoint.sh


FROM alpine:3.9

LABEL maintainer="Akrom Khasani <akrom@volantis.io>"

COPY --from=builder /opt /usr/local/bin/

# Create default user
# Install bash and curl
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 DEFAULT_USER=user
RUN apk add -q --no-progress --no-cache --virtual=.user-creation shadow && \
    useradd -mU -d /home/${DEFAULT_USER} ${DEFAULT_USER} && passwd -d ${DEFAULT_USER} && \
    apk del -q .user-creation && \
    apk add --no-cache bash curl

# Install GNU libc (aka glibc) and set ${LANG} locale as default
# (https://github.com/frol/docker-alpine-glibc)
# (https://github.com/sgerrand/alpine-pkg-glibc)
RUN ALPINE_GLIBC_PACKAGE_VERSION=2.29-r0 && \
    ALPINE_GLIBC_BASE_URL=https://github.com/sgerrand/alpine-pkg-glibc/releases/download && \
    ALPINE_GLIBC_BASE_PACKAGE_FILENAME=glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk && \
    ALPINE_GLIBC_BIN_PACKAGE_FILENAME=glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk && \
    ALPINE_GLIBC_I18N_PACKAGE_FILENAME=glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk && \
    curl -skSL https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub && \
    curl -kSL \
        -O ${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/${ALPINE_GLIBC_BASE_PACKAGE_FILENAME} \
        -O ${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/${ALPINE_GLIBC_BIN_PACKAGE_FILENAME} \
        -O ${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/${ALPINE_GLIBC_I18N_PACKAGE_FILENAME} && \
    apk add --no-cache \
        ${ALPINE_GLIBC_BASE_PACKAGE_FILENAME} \
        ${ALPINE_GLIBC_BIN_PACKAGE_FILENAME} \
        ${ALPINE_GLIBC_I18N_PACKAGE_FILENAME} && \
    rm -f /etc/apk/keys/sgerrand.rsa.pub && \
    /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 ${LANG} || true && \
    echo "export LANG=$LANG" > /etc/profile.d/locale.sh && \
    apk del -q glibc-i18n && \
    rm -f \
        ${ALPINE_GLIBC_BASE_PACKAGE_FILENAME} \
        ${ALPINE_GLIBC_BIN_PACKAGE_FILENAME} \
        ${ALPINE_GLIBC_I18N_PACKAGE_FILENAME}

# Set working directory
VOLUME /tmp
WORKDIR /tmp

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]

# vim:set ft=dockerfile sw=4 ts=4:
