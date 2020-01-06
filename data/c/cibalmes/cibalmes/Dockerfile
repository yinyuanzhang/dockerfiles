FROM ubuntu:18.04

MAINTAINER Samuel Baena, Sara Guijarro

ARG DEBIAN_FRONTEND=newt

RUN apt-get -y update && apt-get install -y \
apache2 \
php7.2 \
libapache2-mod-php7.2 \
php7.2-bcmath \
php7.2-gd \
php7.2-json \
php7.2-sqlite \
php7.2-pgsql \
php7.2-curl \
php7.2-xml \
php7.2-mbstring \
php7.2-zip \
git \
mcrypt \
vim

RUN apt-get install locales
RUN locale-gen en_US.UTF-8
RUN locale-gen es_ES.UTF-8

# Instalar composer
WORKDIR /usr/lib
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php \
&& php -r "unlink('composer-setup.php');"

#Instalar Phpmailer
RUN php /usr/lib/composer.phar require phpmailer/phpmailer @stable

# Config php
# Mostrar errors PHP
RUN sed -i -e 's/^error_reporting\s*=.*/error_reporting = E_ALL/' /etc/php/7.2/apache2/php.ini
RUN sed -i -e 's/^display_errors\s*=.*/display_errors = On/' /etc/php/7.2/apache2/php.ini
RUN sed -i -e 's/^zlib.output_compression\s*=.*/zlib.output_compression = Off/' /etc/php/7.2/apache2/php.ini

# Per usar vim amb "docker exec -it [CONTAINER ID] bash"
ENV TERM xterm

# Config apache
# Permetre reescriure a .htaccess amb RewriteEngine
RUN a2enmod rewrite
# Live logs : docker logs -f [CONTAINER ID]
# Evitar error "AH00558: apache2: Could not reliably determine the server's fully qualified domain name"
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
# Autoritzar .htaccess files
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf
RUN chgrp -R www-data /var/www
RUN find /var/www -type d -exec chmod 775 {} +
RUN find /var/www -type f -exec chmod 664 {} +

EXPOSE 80
EXPOSE 443

# Arrancar Apache2 al iniciar
CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]
