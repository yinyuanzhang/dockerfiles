###
# MeuPatrocinio
# Based on github.com/dev500/docker-thumbor
# Based on github.com/NYTimes/thumbor-docker-image
# Based on github.com/julianbei/alpine-opencv-microimage
#
# Repository:    Python 
# Image:         Webserver
# Version:       2.7
# Strategy:      Python webserver running Thumbor along with New Relic
# Base distro:   Python 2.7 with Alpine 3.6
#

FROM julianbei/alpine-opencv-microimage:p2-3.1 AS build
ENV THUMBOR_VERSION 6.5.2
RUN apk add --upgrade  --no-cache apk-tools@edge
RUN apk add --no-cache libjpeg-turbo-dev libressl-dev libpng-dev tiff-dev curl-dev jasper-dev
RUN pip install --upgrade pip
RUN pip install thumbor==${THUMBOR_VERSION}
RUN ls /usr/local/bin

FROM python:2.7-alpine3.6
LABEL MAINTAINER="Daniel Pinto <daniel@meupatrocinio.com>"
RUN apk add --no-cache \ 
    libjpeg \
    libpng \
    tiff \
    libcurl \
    jasper-dev \
    libstdc++ \
    libdc1394 \
    libwebp \
    libgfortran \
    tk \
    bash \
    curl \
    fontconfig \
    libxrender \
    libxext \
    vim \
    git \
    unzip \
    wget \
    sudo

ADD start.sh /scripts/start.sh
RUN wget -O /tini https://github.com/krallin/tini/releases/download/v0.18.0/tini-static && \
    chmod +x /tini && \
    chmod +x /scripts/start.sh

COPY --from=build /usr/local/lib /usr/local/lib
COPY --from=build /usr/local/lib/python2.7 /usr/lib/python2.7
COPY --from=build /usr/local/bin/thumbor /usr/local/bin/thumbor-config /usr/local/bin/thumbor-url /usr/bin/
COPY --from=build /usr/lib/libopenblas.so.3 /usr/lib/libopenblasp-r0.2.19.so /usr/lib/
COPY thumbor.conf /etc/thumbor.conf
RUN ln -s /usr/local/bin/python /usr/bin/python && \
    pip install newrelic && \
    pip install tc_aws && \
    newrelic-admin generate-config REPLACE_WITH_REAL_KEY newrelic.ini

ENV PYTHONPATH /usr/lib/python2.7/site-packages:/usr/local/lib/python2.7/site-packages

# Define the entry point that tries to enable newrelic
ENTRYPOINT ["/tini", "--", "/scripts/start.sh", "thumbor", "-l", "info", "-p", "80"]
