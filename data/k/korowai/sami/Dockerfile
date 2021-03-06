#############################################################################
# NOTE: FILE GENERATED AUTOMATICALLY, DO NOT EDIT!!!
#############################################################################

FROM php:7.2-alpine

MAINTAINER Paweł Tomulik <ptomulik@meil.pw.edu.pl>

ARG KRW_CODE='/code'
ARG SAMI_CONFIG='/etc/sami/sami.conf.php'
ARG SAMI_PROJECT_TITLE='API Documentation'
ARG SAMI_SOURCE_DIR='src'
ARG SAMI_BUILD_DIR='docs/build/html/api'
ARG SAMI_CACHE_DIR='docs/cache/html/api'
ARG SAMI_FLAGS='-v --force'
ARG SAMI_SERVER_PORT=8001
ARG SAMI_SOURCE_REGEX='\.\(php\|txt\|rst\)$'
ARG SAMI_THEME='default'

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.name="Docker Sami Image" \
      org.label-schema.description="Docker image with Sami documentation generator. Designed to build PHP API docs for Korowai project." \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.vcs-url="https://github.com/korowai/docker-sami" \
      org.label-schema.vendor="Paweł Tomulik" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.schema-version="1.0"


ENV KRW_CODE=$KRW_CODE \
    SAMI_CONFIG=$SAMI_CONFIG \
    SAMI_PROJECT_TITLE=$SAMI_PROJECT_TITLE \
    SAMI_SOURCE_DIR=$SAMI_SOURCE_DIR \
    SAMI_BUILD_DIR=$SAMI_BUILD_DIR \
    SAMI_CACHE_DIR=$SAMI_CACHE_DIR \
    SAMI_FLAGS=$SAMI_FLAGS \
    SAMI_SERVER_PORT=$SAMI_SERVER_PORT \
    SAMI_SOURCE_REGEX=$SAMI_SOURCE_REGEX \
    SAMI_THEME=$SAMI_THEME

RUN set -xe && \
  apk add --no-cache --update inotify-tools git && \
  curl -s -L -o /usr/local/bin/sami http://get.sensiolabs.org/sami.phar && \
  chmod a+x /usr/local/bin/sami && \
  mkdir -p "`dirname \"${SAMI_CONFIG}\"`"

COPY bin/* /usr/local/bin/
COPY etc/sami.conf.php /etc/sami/

VOLUME ${KRW_CODE}
WORKDIR ${KRW_CODE}

ENTRYPOINT [ "sami-entrypoint" ]
CMD [ "autoserve" ]

EXPOSE ${SAMI_SERVER_PORT}

# vim: ft=dockerfile:
