FROM php:7.1-apache
MAINTAINER Webgriffe Srl <support@webgriffe.com>

# Install GD
RUN apt-get update \
    && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
	&& apt-get clean

# Install MCrypt
RUN apt-get update \
    && apt-get install -y libmcrypt-dev \
    && docker-php-ext-install mcrypt \
	&& apt-get clean

# Install Intl
RUN apt-get update \
    && apt-get install -y libicu-dev \
    && docker-php-ext-install intl \
	&& apt-get clean

# Install XDEBUG
ENV XDEBUG_ENABLE 0
RUN pecl config-set preferred_state beta \
    && pecl install -o -f xdebug \
    && rm -rf /tmp/pear \
    && pecl config-set preferred_state stable
COPY ./99-xdebug.ini.disabled /usr/local/etc/php/conf.d/

# Install Memprof
ENV MEMPROF_ENABLE 0
RUN pecl config-set preferred_state beta \
    && apt-get install -y libjudy-dev \
    && pecl install -o -f memprof \
    && rm -rf /tmp/pear \
    && pecl config-set preferred_state stable


# Install Mysql
RUN docker-php-ext-install mysqli pdo_mysql

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# Install mbstring
RUN docker-php-ext-install mbstring

# Install soap
RUN apt-get update \
    && apt-get install -y libxml2-dev \
    && docker-php-ext-install soap \
	&& apt-get clean

# Install opcache
RUN docker-php-ext-install opcache

# Install PHP zip extension
RUN docker-php-ext-install zip

# Install Git
RUN apt-get update \
    && apt-get install -y git \
	&& apt-get clean

# Install xsl
RUN apt-get update \
    && apt-get install -y libxslt-dev \
    && docker-php-ext-install xsl \
	&& apt-get clean

# Define PHP_TIMEZONE env variable
ENV PHP_TIMEZONE Europe/Rome

# Configure Apache Document Root
ENV APACHE_DOC_ROOT /var/www/html

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Additional PHP ini configuration
COPY ./999-php.ini /usr/local/etc/php/conf.d/

# Sample index.php with phpinfo() and entrypoint
COPY ./index.php /var/www/html/index.php

# Install ssmtp Mail Transfer Agent
RUN apt-get update \
    && apt-get install -y ssmtp \
    && apt-get clean \
    && echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf \
    && echo 'sendmail_path = "/usr/sbin/ssmtp -t"' > /usr/local/etc/php/conf.d/mail.ini

# Install MySQL CLI Client & Text Editor
RUN apt-get update \
    && apt-get install -y mysql-client \
    && apt-get install -y vim-tiny \
	&& apt-get clean
	
COPY ./vimrc /root/.vimrc

########################################################################################################################

# Start!
COPY ./start /usr/local/bin/
CMD ["start"]
