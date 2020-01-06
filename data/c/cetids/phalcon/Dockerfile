FROM php:7.0-fpm
MAINTAINER xxz <xxz@cetids.com>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
        libmcrypt-dev \
        libpng12-dev \
        libcurl4-openssl-dev \
        libsqlite3-dev \
	libssl-dev \
        nano \
        bzip2 \
    && docker-php-ext-install -j$(nproc) iconv mcrypt zip pdo pdo_mysql mysqli \
    && docker-php-ext-configure gd --with-png-dir=/usr/include --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd 



RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini


RUN set -ex \
	&& pecl install APCu-5.1.3 \
 	&& pecl install redis-3.1.0 \
    && pecl install xdebug-2.5.0 \
    && docker-php-ext-enable redis apcu xdebug

ENV PHALCON_VERSION=3.0.3

# Compile Phalcon
RUN set -xe && \
        curl -LO https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \
        tar xzf v${PHALCON_VERSION}.tar.gz && cd cphalcon-${PHALCON_VERSION}/build && ./install && \
        echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/phalcon.ini && \
        cd ../.. && rm -rf v${PHALCON_VERSION}.tar.gz cphalcon-${PHALCON_VERSION} && \
        # Insall Phalcon Devtools, see https://github.com/phalcon/phalcon-devtools/
        curl -LO https://github.com/phalcon/phalcon-devtools/archive/v${PHALCON_VERSION}.tar.gz && \
        tar xzf v${PHALCON_VERSION}.tar.gz && \
        mv phalcon-devtools-${PHALCON_VERSION} /usr/local/phalcon-devtools && \
	rm -rf v${PHALCON_VERSION}.tar.gz && \
        ln -s /usr/local/phalcon-devtools/phalcon.php /usr/local/bin/phalcon

COPY ./php7-fpm/php.ini /usr/local/etc/php/php.ini
COPY ./php7-fpm/www.conf /usr/local/etc/php-fpm.d/www.conf
