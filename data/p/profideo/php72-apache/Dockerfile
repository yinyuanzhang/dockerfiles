FROM profideo/php-7.2-fpm

# Install apt-transport-https
RUN apt-get update && apt-get install -y apt-transport-https

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions
RUN apt-get update && apt-get install -y zlib1g-dev libpng-dev
RUN docker-php-ext-install pdo pdo_mysql zip sockets gd

# Install memcached php extension
RUN apt-get -y install libmemcached11 libmemcachedutil2 libmemcached-dev \
    && git clone --branch php7 https://github.com/php-memcached-dev/php-memcached \
    && cd php-memcached \
    && phpize \
    && ./configure \
    && make \
    && mv modules/memcached.so /usr/local/lib/php/extensions/no-debug-non-zts-20170718/ \
    && docker-php-ext-enable memcached

# Install ClamAV
RUN apt-get update && apt-get install -y clamav clamav-freshclam clamav-daemon

# Install nodejs
RUN apt-get install -y software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

# Supervisor
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
