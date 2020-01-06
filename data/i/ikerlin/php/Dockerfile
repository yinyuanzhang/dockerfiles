FROM ikerlin/php:7.1-fpm-supervisor

# Install Swoole
RUN pecl install swoole \
    && docker-php-ext-enable swoole

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*