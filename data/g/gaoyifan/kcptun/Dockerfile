FROM smartentry/alpine:3.6-0.4.0

MAINTAINER Yifan Gao <git@yfgao.com>

COPY .docker $ASSETS_DIR

RUN smartentry.sh build

EXPOSE 29900/udp
