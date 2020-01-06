FROM php:5.6-apache

RUN apt-get update \
        && apt-get install -y software-properties-common \
        && apt-get update \
        && apt-get install -y \
        libmcrypt-dev libpng-dev \
        libmemcached11 libmemcachedutil2 build-essential libmemcached-dev libz-dev \
        librabbitmq4 librabbitmq-dev \
            mysql-client \
            openssl \
            wget \
            git \
            unzip \
            cron \
            vim \
            memcached \
            supervisor \
            sudo \
            acl \
        # memcached ext
        && pecl install memcached-2.2.0 \
        && docker-php-ext-enable memcached \
        # amqp
        && pecl install amqp \
        && docker-php-ext-enable amqp \
        # xdebug
        && pecl install xdebug-2.5.0 \
        && docker-php-ext-enable xdebug \
        # timecop
        && curl -L https://github.com/hnw/php-timecop/archive/master.tar.gz | tar -xz \
        && cd php-timecop-master && phpize && ./configure && make && make install \
        && docker-php-ext-enable timecop \
        # composer
        && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer \
        # cleanup
        && rm -rf /var/lib/apt/lists/* \
        && apt-get remove -y build-essential libmemcached-dev libz-dev \
        && apt-get autoremove -y \
        && rm -rf /tmp/pear

RUN docker-php-ext-install \
        pdo \
        pcntl \
        pdo_mysql \
        mcrypt \
        zip \
        gd

COPY php.ini /usr/local/etc/php/php.ini
COPY default.conf /etc/apache2/sites-enabled/000-default.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf

RUN ln -s /app /var/www/site
RUN a2enmod headers rewrite
RUN systemctl enable memcached
