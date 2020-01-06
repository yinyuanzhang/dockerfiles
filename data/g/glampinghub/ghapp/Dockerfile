FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    TERM=${TERM:-xterm} \
    PORT=8000 \
    ENV=develop \
    PATH=/webapp/venv/bin/:/webapp/.venv/bin/:$PATH \
    DEBUG=True

ADD https://deb.nodesource.com/setup_6.x /tmp/setup-nodejs
COPY ./sd_notify /usr/bin/
COPY ./docker-entrypoint.sh /
COPY ./http_ok-linux-amd64 /usr/local/bin/http_ok

RUN apt-get update \
    && apt-get install locales \
    && locale-gen en_US.UTF-8 \
    && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
    && bash /tmp/setup-nodejs \
    && apt-get install --no-install-recommends -qy \
        nodejs openssh-client git \
        build-essential awscli \
        virtualenv python-pip python-dev python-setuptools python-wheel \
        libpq-dev libmaxminddb0 libmaxminddb-dev libmemcached-dev \
        libjpeg8 libjpeg8-dev libopenjp2-7 libopenjp2-7-dev libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libwebp5 libwebp-dev \
        libgeos-3.5.0 libgeos-dev gdal-bin libgdal-dev python-gdal binutils libproj-dev gdal-bin \
        wkhtmltopdf xvfb \
        libffi-dev \
        vim less jq \
        && ln -s /usr/include/freetype2 /usr/local/include/freetype \
    && echo -n '#!/bin/sh\nxvfb-run -a /usr/bin/wkhtmltopdf "$@" || /usr/bin/wkhtmltopdf "$@"\n' > /usr/local/bin/wkhtmltopdf \
    && chmod +x /usr/local/bin/wkhtmltopdf \
    && npm install --global --production eslint \
    && pip install flake8 flake8_formatter_junit_xml \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && npm cache clean

WORKDIR /webapp
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/sleep","infinity"]

# Metadata
LABEL org.opencontainers.image.authors="José Luis Salvador Rufo <salvador.joseluis@gmail.com>" \
      org.opencontainers.image.title="Django container" \
      org.opencontainers.image.url="https://glampinghub.com" \
      org.opencontainers.image.vendor="Glamping Hub USA Inc."      
