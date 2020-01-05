FROM php:7.2-apache

RUN set -x \
        && apt-get update && apt-get install unzip -y \
        && apt-get install -y libldap2-dev ldap-utils \
        && rm -rf /var/lib/apt/lists/* \
        && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
        && docker-php-ext-install ldap \
        && apt-get purge -y --auto-remove libldap2-dev
RUN a2enmod rewrite


ADD https://github.com/ltb-project/self-service-password/archive/master.zip /
RUN unzip /master.zip -d /var/www/html
RUN mv /var/www/html/self-service-password-master/* /var/www/html
RUN rm -rf /var/www/html/self-service-password-master
RUN chown -R www-data:www-data /var/www/html

VOLUME /var/www/html/conf
