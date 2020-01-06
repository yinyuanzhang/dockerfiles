FROM php:5.6-apache
MAINTAINER Yves Blusseau <90z7oey02@sneakemail.com> (@blusseau)

ENV MAILHUB=postfix-relay

# Copy init and config files
COPY /config /etc/config

# Install PHP extensions
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libpng12-dev libjpeg-dev libmagickwand-dev libxslt1-dev zip unzip patch && \
    patch -d /etc/apache2 < /etc/config/apache2.conf.patch && \
    docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
    docker-php-ext-install gd && \
    docker-php-ext-install calendar && \
    docker-php-ext-install gettext && \
    docker-php-ext-install mbstring && \
    docker-php-ext-install mysql && \
    docker-php-ext-install mysqli && \
    docker-php-ext-install xsl && \
    docker-php-ext-install zip && \
    pecl install imagick-3.4.1 && \
    rm -f /usr/local/etc/php/conf.d/docker-php-ext-* && \
    pear install --alldeps Mail-1.2.0 && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y ssmtp && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false && \
    apt-get clean all && rm -rf /var/lib/apt/lists/*

# Copy init scripts
COPY /entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
