FROM davask/d-http:a2.4-d8.x
MAINTAINER davask <docker@davaskweblimited.com>
USER root
LABEL dwl.app.language="php 7.0"

ENV DWL_PHP_VERSION 7.0
ENV DWL_PHP_DATETIMEZONE Europe/Paris

RUN sed -i 's|^deb http://deb.debian.org/debian jessie main|deb http://deb.debian.org/debian jessie main contrib non-free|g' /etc/apt/sources.list; \
sed -i 's|^deb http://deb.debian.org/debian jessie-updates main|deb http://deb.debian.org/debian jessie-updates main contrib non-free|g' /etc/apt/sources.list; \
sed -i 's|^deb http://deb.debian.org/debian jessie/updates main|deb http://deb.debian.org/debian jessie/updates main contrib non-free|g' /etc/apt/sources.list; \
echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list; \
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list; \
echo 'deb http://deb.debian.org/debian stretch main' >> /etc/apt/sources.list; \
wget https://www.dotdeb.org/dotdeb.gpg -O /tmp/dotdeb.gpg; \
apt-key add /tmp/dotdeb.gpg; \
rm /tmp/dotdeb.gpg;

# Update packages
RUN apt-get update && apt-get install -y \
php7.0 \
php7.0-fpm \
php7.0-mcrypt \
php7.0-mysqlnd \
php7.0-gd \
php7.0-curl \
php7.0-memcached \
php7.0-cli \
php7.0-readline \
php7.0-mysqlnd \
php7.0-json \
php7.0-intl \
php7.0-common \
php7.0-xml \
php7.0-opcache \
php7.0-mbstring \
php7.0-zip \
libssl1.1 \
libapache2-mod-php7.0 \
libapache2-mod-fastcgi \
memcached \
mysql-client

RUN a2enmod actions fastcgi alias proxy_fcgi setenvif
RUN a2enconf php7.0-fpm

RUN apt-get install -y \
sendmail-bin \
sendmail

RUN apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig);
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');";
RUN ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');");
RUN php composer-setup.php; \
mv composer.phar /usr/local/bin/composer;
RUN php -r "unlink('composer-setup.php');";

COPY ./build/dwl/php.sh \
./build/dwl/init.sh \
/dwl/

RUN chmod +x /dwl/init.sh && chown root:sudo -R /dwl
USER admin
