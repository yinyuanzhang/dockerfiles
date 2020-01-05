FROM php:7.2.5-apache
MAINTAINER Cahya Sulianto Wibawa (inbox@cahsul.com)


RUN requirements="nano libmcrypt-dev libmcrypt4 libcurl3-dev libxml2-dev libfreetype6 libjpeg62-turbo libfreetype6-dev libjpeg62-turbo-dev" \
    && apt-get update && apt-get install -y --no-install-recommends $requirements && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo pdo_mysql \
    && docker-php-ext-configure gd --with-flsreetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install soap \
    && docker-php-ext-install mysqli && \
    apt-get update && apt-get install libldap2-dev -y && apt-get install -y libpq-dev && docker-php-ext-install pdo pgsql pdo_pgsql && \
    apt-get install -y git zip unzip && \
    php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure ldap && \
    docker-php-ext-install ldap && \
    apt-get -y autoremove && \
    apt-get clean && \
    requirementsToRemove="libmcrypt-dev libcurl3-dev libxml2-dev  libfreetype6-dev libjpeg62-turbo-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove


# SSL
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/ssl-cert-snakeoil.key -out /etc/ssl/certs/ssl-cert-snakeoil.pem -subj "/C=AT/ST=Vienna/L=Vienna/O=Security/OU=Development/CN=example.com"

RUN chmod -R 777 /var/www/

RUN a2enmod rewrite

RUN a2ensite default-ssl

RUN a2enmod ssl

RUN a2enmod headers


# SQL SERVER
RUN apt-get update && apt-get install -y apt-transport-https curl &&apt-get install -y gpg && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && apt-get update && curl https://packages.microsoft.com/config/debian/9/prod.list | tee /etc/apt/sources.list.d/mssql-tools.list && apt-get update && ACCEPT_EULA=Y apt-get install --yes --assume-yes mssql-tools  && apt-get install -y unixodbc-dev && pecl install sqlsrv-5.2.0 pdo_sqlsrv-5.2.0 && pecl install sqlsrv pdo_sqlsrv

COPY ./src/start.sh ./

RUN chmod +x ./start.sh

RUN /bin/bash -c "source ./start.sh"


# CONFIG
COPY ./src/php.ini /usr/local/etc/php/

COPY ./src/.htaccess /var/www/html


EXPOSE 80

EXPOSE 443
