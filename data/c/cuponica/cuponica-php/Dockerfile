FROM ubuntu:18.04
MAINTAINER Ebowe <info@ebowe.com>

ENV DEBIAN_FRONTEND=noninteractive

# Repositorio de PHP
COPY docker-files/ondrej.pgp /root/ondrej.pgp

# Core
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y ca-certificates curl gnupg git openssh-client

# Instalo el repositio ondrej y saco todo lo que no uso!
RUN cat /root/ondrej.pgp | apt-key add && \
        printf "deb [arch=amd64] http://ppa.launchpad.net/ondrej/php/ubuntu bionic main\n" > /etc/apt/sources.list.d/ondrej.list && \
    rm -f /root/ondrej.pgp

# PHP requerido para Cuponica
RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    apache2 \
    php5.6 php5.6-dev php5.6-curl \
    php5.6-bcmath php5.6-bz2 php5.6-gd php5.6-gmp php5.6-intl \
    php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-opcache \
    php5.6-soap php5.6-xml php5.6-xmlrpc php5.6-xsl php5.6-zip php5.6-sqlite3

# Instalo adicionales post PHP:
RUN apt-get install -y --no-install-recommends --no-install-suggests \
    geoip-bin php-geoip php-pear composer make php-apcu php-memcache php-memcached php-imagick

# Pecl builds
RUN pecl install -f stem && \
    echo extension=stem.so > /etc/php/5.6/mods-available/stem.ini  && \
    ln -s /etc/php/5.6/mods-available/stem.ini /etc/php/5.6/apache2/conf.d && \
    ln -s /etc/php/5.6/mods-available/stem.ini /etc/php/5.6/cli/conf.d/

RUN a2enmod php5.6
RUN a2enmod rewrite
RUN a2enmod headers

# Cleanup
RUN apt-get -y --purge autoremove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/{man,doc}

# make the webroot a volume
VOLUME /var/www/html/

EXPOSE 80

CMD /usr/sbin/apache2ctl -D FOREGROUND