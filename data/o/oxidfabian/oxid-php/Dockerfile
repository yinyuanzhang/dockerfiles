FROM php:7.3-fpm

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp
ENV INSTALL_SHOP true

# install dependencies and cleanup (needs to be one step, as else it will cache in the laver)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    git msmtp default-mysql-client iproute2 libfreetype6 libjpeg62-turbo libcurl4-openssl-dev libjpeg-dev libpng-dev libxml2-dev libmemcached-dev libzip-dev sudo && \
    pecl install xdebug memcached && \
    docker-php-ext-enable xdebug && \
    docker-php-ext-configure gd --with-jpeg-dir=/usr/local/ && \
    docker-php-ext-install -j$(nproc) curl json xml mbstring zip bcmath soap pdo_mysql gd mysqli && \
    apt-get clean && \
    apt-get autoremove -y && \
    apt-get purge -y --auto-remove libcurl4-openssl-dev libjpeg-dev libpng-dev libxml2-dev libmemcached-dev && \
    rm -rf /var/lib/apt/lists/*

# configure PHP
RUN touch /usr/local/etc/php/conf.d/php.ini; \
        echo memory_limit=512M >> /usr/local/etc/php/conf.d/php.ini

# configure xdebug
RUN touch /usr/local/etc/php/conf.d/xdebug.ini; \
	echo xdebug.remote_enable=1 >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.remote_autostart=0 >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.remote_port=9001 >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.remote_host=host.docker.internal >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.idekey=PHPSTORM >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.remote_handler=dbgp >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.profiler_enable_trigger = 1 >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.profiler_output_dir=/var/www/html/ >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo xdebug.trace_enable_trigger_value="XDEBUG_PROFILE" >> /usr/local/etc/php/conf.d/xdebug.ini; \
  	echo date.timezone = Europe/Berlin >> /usr/local/etc/php/conf.d/timezone.ini

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# set up mailhog as sendmail target
RUN echo "host mailhog" >> /etc/msmtprc
RUN echo "port 1025" >> /etc/msmtprc
RUN echo "sendmail_path=/usr/bin/msmtp -t" >> /usr/local/etc/php/conf.d/php-sendmail.ini

COPY config.inc.php /var/www/config.inc.php
COPY docker-php-entrypoint /usr/local/bin/

RUN export PHP_IDE_CONFIG="serverName=Docker"

RUN chmod 777 /usr/local/bin/docker-php-entrypoint \
    && ln -s /usr/local/bin/docker-php-entrypoint /