FROM php:7-apache
# https://github.com/NatLibFi/Skosmos/wiki/Installation

RUN apt-get update -y && \
    apt-get install -y git php-gettext unzip vim wget && \
	cd /tmp && wget https://github.com/NatLibFi/Skosmos/archive/v1.7.zip && \
	unzip v1.7.zip && rm v1.7.zip && \
    rmdir /var/www/html && \
    mv Skosmos-1.7 /var/www/html && cd /var/www/html && \
    mv config.inc.dist config.inc && mv vocabularies.ttl.dist vocabularies.ttl && \
    docker-php-ext-install gettext && \
    wget https://getcomposer.org/composer.phar && \
    a2enmod rewrite && \
    php composer.phar install --no-dev 

#setsebool -P httpd_can_network_connect on
#https://github.com/NatLibFi/Skosmos/wiki/Configuration
