FROM php:7.2-apache

RUN apt-get update && \
    apt-get install -y --no-install-recommends libjpeg-dev libpng-dev libwebp-dev libc-client-dev libkrb5-dev libpq-dev git libldb-dev libldap2-dev libbz2-dev && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

RUN docker-php-ext-configure gd \
      --with-jpeg-dir=/usr/include \
      --with-png-dir=/usr/include \
      --with-webp-dir=/usr/include && \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \
    docker-php-ext-install pdo_mysql pdo_pgsql gd ldap zip imap
    
WORKDIR /var/www/html

RUN curl -L https://github.com/LimeSurvey/LimeSurvey/archive/3.17.6+190624.tar.gz -s -o - | tar -xz --strip-components 1 -f -

RUN chmod -R go+w tmp && \
    chmod -R go+w upload && \
    chmod -R go+w application/config && \
    mkdir -p sessions && \
    chmod 755 sessions && chown www-data sessions && \
    echo "php_value session.save_handler \"files\"" >> .htaccess && \
    echo "php_value session.save_path \"/var/www/html/sessions\"" >> .htaccess

EXPOSE 80
