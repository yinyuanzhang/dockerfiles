FROM php:apache
RUN apt-get update && apt-get install -y --no-install-recommends certbot python-certbot-apache
RUN a2enmod ssl headers rewrite proxy proxy_http proxy_wstunnel && a2ensite default-ssl
COPY *.php /usr/share/php/libphp-phpmailer/
