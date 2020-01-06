FROM ubuntu:12.04
MAINTAINER Oleksand Bazylevych <oleksandr.bazylevych@gmail.com>

VOLUME ["/var/www"]

RUN apt-get update && \
    apt-get install -y \
      git \
      apache2 \
      php5 \
      php5-cli \
      libapache2-mod-php5 \
      php5-gd \
      php5-imagick \
      php5-intl \
      php5-xdebug \
      php5-ldap \
      php5-mysql \
      php5-pgsql \
      php5-mcrypt \
      php5-curl \
      curl \
      nano \
      htop \
      mc

COPY apache_default /etc/apache2/sites-available/default
COPY run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run
RUN a2enmod rewrite

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

EXPOSE 80
CMD ["/usr/local/bin/run"]
