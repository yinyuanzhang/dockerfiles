## Dockerfile
## https://docker.github.io/engine/reference/builder/
FROM debian:10-slim

ARG DEBIAN_FRONTEND=noninteractive
ARG user=worker
ARG port=8080

RUN set -ex; \
    groupadd --system ${user} && \
    useradd --system --gid ${user} ${user}

## Install runtime
RUN set -ex; \
    apt-get update && apt-get install --yes --no-install-recommends \
        ca-certificates \
        uwsgi \
        uwsgi-plugin-php \
        php7.3-cli \
        php7.3-json \
        php7.3-gd \
        php7.3-curl \
        php7.3-mysql \
        php7.3-xml \
        php7.3-mbstring \
        php7.3-intl \
        php7.3-opcache \
        php-redis \
        php-imagick \
    && rm -rf /var/lib/apt/lists/*

ENV PORT=${port}
ENV USER=${user}

## Setup dukuwiki
ADD https://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz /tmp/dokuwiki-stable.tar.gz
RUN set -ex; \
    mkdir -p /opt/source/public_html/ \
    && mkdir -p /opt/source/dokuwiki/ \
    && tar xvf /tmp/dokuwiki-stable.tar.gz -C /opt/source/public_html --strip-components 1 \
    && chown -R ${user}:${user} /opt/source/public_html \
    && tar cvf /opt/dokuwiki-data.tar.gz -C /opt/source/public_html/ data/ conf/ \
    && rm -rf /opt/source/public_html/conf \
    && rm -rf /opt/source/public_html/data \
    && rm /tmp/*.tar.gz

ADD uwsgi.ini /opt/config/uwsgi.ini
ADD php.ini /opt/config/php.ini
ADD entrypoint.sh /opt/entrypoint.sh

EXPOSE ${PORT}
WORKDIR /opt
CMD []
ENTRYPOINT ["/opt/entrypoint.sh"]
