FROM lsiobase/alpine:3.8

ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="xyzzyx"
MAINTAINER xyzzyx

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

RUN \
    echo "**** install build packages ****" && \
    apk add --no-cache --virtual=build-dependencies \
        autoconf \
        automake \
        freetype-dev \
        g++ \
        gcc \
        jpeg-dev \
        lcms2-dev \
        libffi-dev \
        libpng-dev \
        libwebp-dev \
        linux-headers \
        make \
        openjpeg-dev \
        openssl-dev \
        python3-dev \
        tiff-dev \
        zlib-dev \
        git && \
    echo "**** install runtime packages ****" && \
    apk add --no-cache \
        python3 \
        tar \
        xz \
        bzip2 \
        zlib \
        gnupg \
        openssl && \
    echo "**** install pip packages/requirements ****" && \
    git clone https://github.com/ProgVal/Limnoria.git /tmp/Limnoria && \
    cd /tmp/Limnoria && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir pyyaml msgpack peewee redis && \
    echo "**** install limnoria ****" && \
    python3 ./setup.py install && \
    cd /usr/lib/python3.6/site-packages/supybot && \
    echo "**** clean up ****" && \
    apk del --purge \
        build-dependencies && \
    rm -rf \
        /root/.cache \
        /tmp/*
COPY root/ /

EXPOSE 8080
