FROM php:7.4-fpm
MAINTAINER Krzysztof Kabala <krzysztof.kabala@amsterdam-standard.pl>

RUN echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo 'alias ll="ls -la"' >> ~/.bashrc

# install & cleanup
RUN apt-get update && apt-get install -y \
    libzip-dev zlib1g-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
	libicu-dev libxml2-dev \
	libz-dev libmemcached-dev libonig-dev libzip-dev \
	libffi-dev libssl-dev \
	git zip cron sudo locales gettext \
	vim && \
	apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*

COPY ./files/* /files/

RUN docker-php-ext-configure mbstring && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install calendar gd iconv bcmath fileinfo intl gettext zip pdo_mysql opcache && \
    pecl install mongodb && \
    docker-php-ext-enable mongodb && \
    cp /files/php.ini /usr/local/etc/php/php.ini

WORKDIR /opt

RUN chown www-data:www-data -R /var/www && ln -s /files/entrypoint.sh /usr/local/bin/entrypoint

RUN curl -sSf https://yake.amsdard.io/install.sh | sudo -E bash

ENTRYPOINT ["/files/entrypoint.sh"]

CMD ["php-fpm"]
