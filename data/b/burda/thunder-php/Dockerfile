FROM php:7.3-cli-stretch

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install required libraries and packages
RUN set -xe; \
    \
    apt-get update; \
    \
    apt-get install -y --no-install-recommends \
        git \
        libfreetype6-dev \
        libjpeg-dev \
        libpng-dev \
        libpq-dev \
        libzip-dev \
    ; \
    \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
    ; \
    \
    docker-php-ext-install \
        gd \
        opcache \
        pcntl \
        pdo_mysql \
        pdo_pgsql \
        zip \
    ; \
    \
    apt list --installed | grep -o '.*-dev' | xargs apt-get purge -y; \
    \
    apt-get clean; \
    \
    rm -rf /var/lib/apt/lists/*;

# Setup PHP Cli OpCache
RUN { \
        echo 'opcache.enable=1'; \
        echo 'opcache.enable_cli=1'; \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=10000'; \
		echo 'opcache.validate_timestamps=0'; \
		echo 'opcache.fast_shutdown=1'; \
	} >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini;

# Install composer
RUN set -xe; \
    \
    curl https://getcomposer.org/installer --output composer-setup.php; \
    \
    php composer-setup.php; \
    \
    rm -rf composer-setup.php; \
    \
    mv ./composer.phar /usr/local/bin/composer; \
    \
    chmod +x /usr/local/bin/composer;

ENTRYPOINT ["docker-php-entrypoint"]
CMD ["php", "-a"]
