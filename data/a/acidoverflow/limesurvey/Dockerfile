FROM php:7.2-apache

ARG version='3.16.1+190314'
ARG sha256_checksum='3eb5c9046b7a5991dd5457e9801340db833c401c18332e094d5582d377989548'

RUN apt-get update && \
    apt-get install -y  \
    libc-client-dev \
    libkrb5-dev \
    libpng-dev \
    libldap2-dev \
    && \
    rm -r /var/lib/apt/lists/*

RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install \
    gd \
    imap \
    ldap \
    mbstring \
    pdo \
    pdo_mysql \
    zip

ADD conf/apache2.conf /etc/apache2/conf/apache2.conf
ADD conf/000-default.conf /etc/apache2/sites-available/
ADD conf/ports.conf /etc/apache2/ports.conf
# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
# Override with custom opcache settings
COPY conf/memorySettings.ini $PHP_INI_DIR/conf.d/

RUN curl "https://www.limesurvey.org/stable-release?download=2536:limesurvey${version}.tar.gz" -L -o /tmp/limesurvey${version}.tar.gz

RUN set -ex; \
        echo "${sha256_checksum} /tmp/limesurvey${version}.tar.gz" | sha256sum -c - && \
        tar xzf "/tmp/limesurvey${version}.tar.gz" --strip-components=1 -C /var/www/html/ && \
        rm -f "/tmp/limesurvey${version}.tar.gz" && \
        mkdir -p /var/www/html/tmp/runtime && \
        chown -R www-data:root /var/www/html && \
        chmod -R 775 /var/www/html

EXPOSE 8080
USER www-data

CMD ["apache2-foreground"]
VOLUME ["/var/www/html/upload/"]
