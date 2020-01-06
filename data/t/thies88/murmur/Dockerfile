FROM thies88/base-alpine

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="base-alpine-murmur version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="Thies88"

# add local files for our application
COPY root/ /

# environment settings
#ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

RUN mkdir -p /run/murmur && \
apk add --no-cache --update murmur && \
rm -rf /var/cache/apk/*

VOLUME ["/config"]

EXPOSE 64738 64738/udp
