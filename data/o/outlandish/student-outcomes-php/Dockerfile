FROM php:7.1-fpm

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && \
    apt-get install git zip unzip -y
    
RUN apt-get update && \
    apt-get install libpq-dev zlib1g-dev g++ -y && \
    docker-php-ext-install pdo pgsql pdo_pgsql && \
    apt-get remove -y g++ 
    
 RUN apt-get update && \
     apt-get install zlib1g-dev libicu-dev g++ -y && \
     docker-php-ext-configure intl && \
     docker-php-ext-install intl && \
     apt-get remove -y g++

RUN apt-get update && apt-get install libcurl4-openssl-dev -y \
    && docker-php-ext-install curl \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false libcurl4-openssl-dev -y

RUN apt-get update && apt-get install -y \
        zlib1g-dev zlib1g \
    && docker-php-ext-install zip \
    && apt-get remove -y \
        zlib1g-dev

RUN apt-get update && apt-get install -y \
        libmcrypt-dev libmcrypt4 \
    && docker-php-ext-install mcrypt \
    && apt-get remove -y \
        libmcrypt-dev

RUN echo "date.timezone=Europe/London" > /usr/local/etc/php/conf.d/zz-custom.ini

ENV PATH "$PATH:/var/www/html/vendor/bin"

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"
    
RUN curl -OL https://github.com/phpmetrics/PhpMetrics/releases/download/v2.3.2/phpmetrics.phar && \
    chmod +x phpmetrics.phar && \
    mv phpmetrics.phar /usr/local/bin/phpmetrics

RUN curl -OL http://www.phpdoc.org/phpDocumentor.phar && \
    chmod +x phpDocumentor.phar && \
    mv phpDocumentor.phar /usr/local/bin/phpdoc
    
RUN apt-get update \
    && apt-get install -y autoconf g++ make \
    && pecl install xdebug-2.5.5 \
    && docker-php-ext-enable xdebug \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_enable_trigger=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_output_dir=/app/profiling" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && apt-get remove -y autoconf g++ make
    
RUN touch /.composer && \
    chgrp -R 0 /.composer && \
    chmod -R g=u /.composer
