FROM rwindegger/php:fpm

MAINTAINER rene@windegger.wtf

ENV PIWIK_VERSION 3.3.0

ENV GPG_KEYS 814E346FA01A20DBB04B6807B5DBD5925590A237

RUN curl -fsSL -o piwik.tar.gz \
      "https://builds.matomo.org/piwik-${PIWIK_VERSION}.tar.gz" \
 && curl -fsSL -o piwik.tar.gz.asc \
      "https://builds.matomo.org/piwik-${PIWIK_VERSION}.tar.gz.asc" \
 && export GNUPGHOME="$(mktemp -d)" \
 && ( gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \
  || gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEYS" \
  || gpg --keyserver keyserver.pgp.com --recv-keys "$GPG_KEYS" ) \
 && gpg --batch --verify piwik.tar.gz.asc piwik.tar.gz \
 && tar -xzf piwik.tar.gz -C /usr/src/ \
 && rm -rf "$GNUPGHOME" piwik.tar.gz.asc piwik.tar.gz

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# WORKDIR is /var/www/html (inherited via "FROM php")
# "/entrypoint.sh" will populate it at container startup from /usr/src/piwik
VOLUME /var/www/html

ENTRYPOINT ["/entrypoint.sh"]
CMD ["php-fpm"]
