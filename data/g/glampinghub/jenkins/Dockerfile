FROM jenkins/jenkins:lts-alpine
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>

USER root

RUN addgroup --gid 233 docker && addgroup jenkins docker \
    && apk update \
    && apk add \
        git-lfs \
        docker \
        findutils procps \
        npm \
        py2-virtualenv \
        # Python 2 system dependencies
        mariadb-connector-c-dev postgresql-dev gcc python2-dev musl musl-dev libffi-dev \
        # Pillow dependencies
        jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev \
    && echo "@edgecommunity http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && apk add \
        # Chromium
        chromium@edge nss@edge \
    && rm -rf /var/cache/apk/*

USER jenkins
