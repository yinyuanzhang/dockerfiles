FROM eboraas/apache

RUN apt-get update && \
    apt-get upgrade -y && \
    BUILD_PACKAGES="curl supervisor php5 php-apc php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-sybase" && \
    apt-get -y install $BUILD_PACKAGES && \
    apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && \
    curl -L https://phar.phpunit.de/phpunit.phar -o phpunit.phar && chmod +x phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit