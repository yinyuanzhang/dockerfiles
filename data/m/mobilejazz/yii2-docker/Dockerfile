FROM ubuntu:14.04.5

# Update
RUN apt-get -y update
RUN apt-get -y upgrade

# Install supervisor
RUN apt-get install -y supervisor

# Install command line utils
RUN apt-get install -y curl mcrypt git gawk wget vim

# Install apache
RUN apt-get install apache2 -y
RUN mkdir /var/run/apache2
RUN mkdir /var/lock/apache2

# Enable apache rewrites
RUN a2enmod rewrite
RUN a2enmod cgi

# Install Imagemagick
RUN apt-get install -y imagemagick

# Install PHP 5 and some common extensions
RUN apt-get install -y libapache2-mod-php5 php5-common php5-gd php5-dev php-pear php5-xdebug php5-mysql php5-curl aha php5-intl

# Enable mcrypt
RUN php5enmod mcrypt

# Disable xdebug for composer and other cli invocations
RUN php5dismod -s cli xdebug

# Install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Setup xdebug
ADD xdebug/xdebug.ini /etc/php5/mods-available/xdebug.ini
ADD xdebug/xdebug.mac.ini /etc/php5/mods-available/xdebug.mac.ini

# User Stuff
RUN usermod -u 1000 www-data
RUN chown www-data:www-data /usr/local/bin/composer
RUN mkdir -p /var/www/html
RUN chown -R www-data:www-data /var/www

# Apache configuration file
RUN rm /etc/apache2/sites-available/000-default.conf
ADD apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf

# Customised php.ini with better defaults for error reporting etc.
ADD php/php.ini /etc/php5/apache2/php.ini

# Apache ENVVARS
ADD apache2/envvars /etc/apache2/envvars
# Supervisord configuration file
ADD supervisord/apache2.conf /etc/supervisor/conf.d/apache2.conf

# Run scripts
ADD scripts/run.sh /run.sh
ADD scripts/run-mac.sh /run-mac.sh
ADD scripts/start-apache2.sh /start-apache2.sh
ADD scripts/exec-www.sh /exec-www.sh

RUN chmod 777 /run.sh
RUN chmod 777 /run-mac.sh
RUN chmod 777 /start-apache2.sh
RUN chmod 777 /exec-www.sh

# Install some global composer dependencies
RUN /exec-www.sh composer global require 'hirak/prestissimo:^0.3'

# Data volumnes
VOLUME '/var/www/html'

# Ports
EXPOSE 80 443

# Start
CMD ["/run.sh"]
