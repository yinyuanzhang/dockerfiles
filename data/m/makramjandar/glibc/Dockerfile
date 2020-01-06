FROM alpine

ARG BUILD_DATE
ARG VCS_REF
ARG URL
ARG VERSION

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/makramjandar/AwesomeScripts.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      maintainer="Makram Jandar <makramjandar@gmail.com>"

# Install GNU libc (aka glibc) and set C.UTF-8 locale as default.
RUN URL=$URL && VERSION=$VERSION \
    && apk add --no-cache --virtual=.build-dependencies wget ca-certificates \
    && wget 'https://raw.githubusercontent.com/sgerrand/alpine-pkg-node-bower/master/sgerrand.rsa.pub' -P /etc/apk/keys/ \
    && wget $URL/$VERSION/glibc-$VERSION.apk $URL/$VERSION/glibc-bin-$VERSION.apk $URL/$VERSION/glibc-i18n-$VERSION.apk \
    && apk add --no-cache glibc-$VERSION.apk glibc-bin-$VERSION.apk glibc-i18n-$VERSION.apk \
    && /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true \
    && echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \
    && apk del .build-dependencies glibc-i18n \
    && rm '/root/.wget-hsts' '/etc/apk/keys/sgerrand.rsa.pub' *glibc*.apk
