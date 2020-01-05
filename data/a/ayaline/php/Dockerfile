FROM php:7.0-cli

RUN echo "date.timezone = Europe/Paris" >> /usr/local/etc/php/php.ini
RUN echo "memory_limit = 512M" >> /usr/local/etc/php/php.ini
RUN echo "realpath_cache_size = 4M" >> /usr/local/etc/php/php.ini

RUN apt-get update \
    && apt-get install -y \
            git \
            libfreetype6-dev \
            libjpeg62-turbo-dev \
            libmcrypt-dev \
            libpng12-dev \
            libsqlite3-dev \
            libssl-dev \
            libcurl3-dev \
            libxml2-dev \
            libzzip-dev \
            libicu-dev \
            libxslt-dev \
    && curl -L -o /tmp/apcu-5.1.2.tgz https://pecl.php.net/get/apcu-5.1.2.tgz \
        && tar xfz /tmp/apcu-5.1.2.tgz \
        && rm -r /tmp/apcu-5.1.2.tgz \
        && mv apcu-5.1.2 /usr/src/php/ext/apcu \
    && docker-php-ext-install apcu bcmath iconv intl json mcrypt mbstring mysqli pdo_mysql pdo_sqlite opcache phar xsl curl ftp hash session simplexml tokenizer xml xmlrpc zip \
       && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
       && docker-php-ext-install gd \
    && php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
        && chmod +x /usr/local/bin/composer

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini
