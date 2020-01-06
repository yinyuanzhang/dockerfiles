FROM nimmis/apache

MAINTAINER nimmis <kjell.havneskold@gmail.com>

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
apt-get install -y sudo php libapache2-mod-php php-mongodb \
php-fpm php-cli php-mysqlnd php-pgsql php-sqlite3 php-redis \
php-apcu php-intl php-imagick php-mcrypt php-json php-gd php-curl && \
phpenmod mcrypt && \
rm -rf /var/lib/apt/lists/* && \
cd /tmp && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer
RUN  echo "DirectoryIndex index.php" >> /etc/apache2/apache2.conf
RUN  echo "ServerName 3307.dlinkddns.com" >> /etc/apache2/apache2.conf

RUN a2enmod rewrite
