FROM php:5-apache-jessie

# Since https://github.com/docker-library/php/pull/542
# RUN rm /etc/apt/preferences.d/no-debian-php

RUN apt update \
    && apt install \
       zlib1g-dev libicu-dev \
       mysql-client \
       wget zip \
       # used for i18n during ./setup.sh
       gettext \
       libmcrypt-dev \
       git \
       -y && \
    apt-get clean && apt-get autoclean && apt-get autoremove --purge -y && \
    rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure intl && \
    docker-php-ext-install -j$(nproc) pcntl intl calendar mysql mysqli mcrypt pdo pdo_mysql && \
    echo "date.timezone = \"Europe/Paris\"" >> /usr/local/etc/php/php.ini && \
    echo "display_errors = On" >> /usr/local/etc/php/php.ini && \
    echo "display_startup_errors = On" >> /usr/local/etc/php/php.ini

# RUN pecl install xdebug-2.5.5
# RUN docker-php-ext-enable xdebug

# Add and decompress local file to /tmp. Zend will not change so why download at every build ?
ADD lib/ZendFramework-1.12.20.tar.gz /tmp/
RUN mkdir -p /usr/share/php && mv /tmp/ZendFramework-1.12.20/library/Zend /usr/share/php/ && rm -rf /tmp/*

ADD lib/wait-for-it.sh /opt/

RUN echo 'alias ll="ls -alh"' >> ~/.bashrc \
    && a2enmod rewrite

# Added for backoffice
RUN a2enmod ssl
ADD lib/Zend-Framework-1-Library--Zendx.tar.gz /usr/share/php/ZendX

EXPOSE 80
# CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
