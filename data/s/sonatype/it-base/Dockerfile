FROM       openjdk:8-alpine
MAINTAINER Sonatype <dev@sonatype.com>

ENV GLIBC_VERSION=2.27-r0 \
    DOCKERIZE_VERSION=v0.6.1

# interpolated settings need to go in separate layer
ENV GLIBC_URL=https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION} \
    DOCKERIZE_URL=https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz

RUN apk upgrade --update \
 && apk add --update bash curl ca-certificates \
 && for pkg in glibc glibc-bin glibc-i18n; do \
      curl -sSL ${GLIBC_URL}/${pkg}-${GLIBC_VERSION}.apk -o /tmp/${pkg}.apk; \
    done \
 && apk add --allow-untrusted /tmp/*.apk \
 && rm -v /tmp/*.apk \
 && /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \
 && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \
 && curl -sSL ${DOCKERIZE_URL} | tar -C /usr/local/bin -xz
