FROM php:7.0-apache

RUN a2enmod rewrite

RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev libfreetype6-dev mysql-client \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr \
	&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip exif

RUN pecl install redis-3.1.0 \
    && pecl install xdebug-2.5.0 \
    && docker-php-ext-enable redis xdebug

RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
        echo 'post_max_size=250M'; \
        echo 'upload_max_filesize=250M'; \
        echo 'memory_limit=512M'; \
        echo 'session.cache_limiter = nocache'; \
        echo 'session.auto_start = 0'; \
        echo 'expose_php = off'; \
        echo 'magic_quotes_gpc = off'; \
        echo 'register_globals = off'; \
        echo ''; \
    } > /usr/local/etc/php/conf.d/user-php.ini

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs build-essential

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
