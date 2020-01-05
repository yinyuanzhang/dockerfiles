############################################################
# Dockerfile to build Nextcloud Apache Image
# based on Original nextcloud Image
############################################################
# Container nextcloud
############################################################

# Set the base Image
#FROM nextcloud:13.0.4
#FROM nextcloud:13.0.5
#FROM nextcloud:13.0.6
#FROM nextcloud:14.0.0
#FROM nextcloud:14.0.1
#FROM nextcloud:14.0.2
#FROM nextcloud:14.0.3
#FROM nextcloud:14.0.4
#FROM nextcloud:14.0.6
#FROM nextcloud:15.0.2
#FROM nextcloud:15.0.5
#FROM nextcloud:15.0.8
#FROM nextcloud:15.0.11
#FROM nextcloud:16.0.4
#FROM nextcloud:16.0.7
FROM nextcloud:17.0.2


# File Author / Maintainer
MAINTAINER Sven Berger

RUN set -ex; \
    \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        libmagickcore-6.q16-3-extra \
        procps \
        smbclient \
        supervisor \
 #      libreoffice \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN set -ex; \
    \
    savedAptMark="$(apt-mark showmanual)"; \
    \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        libbz2-dev \
        libc-client-dev \
        libgmp3-dev \
        libkrb5-dev \
        libsmbclient-dev \
        \
# Änderung für Outh (Grauphel)
        libpcre++-dev \
# Änderung für Outh (Grauphel)
        \
    ; \
    \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl; \
#    ln -s "/usr/include/$(dpkg-architecture --query DEB_BUILD_MULTIARCH)/gmp.h" /usr/include/gmp.h; \
    docker-php-ext-install \
        bz2 \
#        gmp \
        imap \
    ; \
    pecl install smbclient; \
    docker-php-ext-enable smbclient; \
    \
# Änderung für Outh (Grauphel)
    pecl install oauth; \
    docker-php-ext-enable oauth; \
# Änderung für Outh (Grauphel)
    \
    apt-mark auto '.*' > /dev/null; \
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
    apt-mark manual $savedAptMark; \
    ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
        | awk '/=>/ { print $3 }' \
        | sort -u \
        | xargs -r dpkg-query -S \
        | cut -d: -f1 \
        | sort -u \
        | xargs -rt apt-mark manual; \
    \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p \
    /usr/share/man/man1 \
    /var/log/supervisord \
    /var/run/supervisord \
;

COPY scripte/supervisord.conf /etc/supervisor/supervisord.conf

ENV NEXTCLOUD_UPDATE=1

CMD ["/usr/bin/supervisord"]
