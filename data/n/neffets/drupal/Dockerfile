# from https://www.drupal.org/docs/8/system-requirements/drupal-8-php-
requirements  
FROM php:7.2-apache  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
if command -v a2enmod; then \  
a2enmod rewrite; \  
fi; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libgmp-dev \  
libjpeg-dev \  
libpng-dev \  
libpq-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install -j "$(nproc)" \  
bcmath \  
gd \  
gmp \  
opcache \  
pdo_mysql \  
pdo_pgsql \  
zip \  
; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
apt-get install -y --no-install-recommends curl tidy mysql-client vim git
msmtp msmtp-mta; \  
rm -rf /var/lib/apt/lists/*  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini ; \  
{ \  
echo 'mbstring.http_input="pass"'; \  
echo 'mbstring.http_output="pass"'; \  
echo 'sendmail_path="/usr/bin/msmtp --file /etc/msmtprc -t -i"'; \  
echo 'display_errors="stdout"'; \  
} > /usr/local/etc/php/conf.d/php-overwrite.ini; \  
{ \  
echo 'host example.com'; \  
echo 'from server@localhost'; \  
echo 'maildomain example.com'; \  
echo 'syslog off'; \  
} > /etc/msmtprc  
  
WORKDIR /var/www/html  
  
# https://www.drupal.org/node/3060/release  
ENV DRUPAL_VERSION 8.5.3  
ENV DRUPAL_MD5 aedc6598b71c5393d30242b8e14385e5  
  
RUN curl -fSL
"https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \  
&& tar -xz --strip-components=1 -f drupal.tar.gz \  
&& rm drupal.tar.gz \  
&& chown -R www-data:www-data sites modules themes  
  
# vim:set ft=dockerfile:  
