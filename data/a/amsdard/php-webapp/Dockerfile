FROM php:7-apache
MAINTAINER Krzysztof Kabala <krzysztof.kabala@amsterdam-standard.pl>

COPY ./files/* /files/

RUN a2enmod rewrite && \
    echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo 'alias ll="ls -la"' >> ~/.bashrc && \
    # install & cleanup
    apt-get update && apt-get install -y \
    libzip-dev zlib1g-dev libonig-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev libzip-dev \
	libicu-dev libxml2-dev \
	libz-dev libmemcached-dev \
	libffi-dev libssl-dev \
	git zip cron sudo locales gettext \
	vim && \
	apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/* && \
    # configure plugins
    docker-php-ext-configure mbstring && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install calendar gd iconv bcmath fileinfo intl gettext zip pdo_mysql opcache && \
    pecl install mongodb && \
    docker-php-ext-enable mongodb && \
    cp /files/php.ini /usr/local/etc/php/php.ini && \
    # ImageMagick
    curl -fsSL 'http://www.imagemagick.org/download/ImageMagick.tar.gz' -o ImageMagick.tar.gz && \
    tar xvzf ImageMagick.tar.gz && \
    cd ImageMagick-* && ./configure && make && make install && /sbin/ldconfig /usr/local/lib && \
    cd .. && rm -rf ImageMagick.tar.gz ImageMagick-* && \
    POLICY_XML_LOCATION="$(find /usr/local/etc/ -name 'policy.xml')" && \
    cp /files/imagemagick-policy.xml $POLICY_XML_LOCATION && \
    # pecl packages
    pecl install imagick && \
    yes '' | pecl install -f redis && \
    docker-php-ext-enable imagick redis && \
    mkdir $PHP_INI_DIR/conf-available && \
    # yake install
    curl -sSf https://yake.amsdard.io/install.sh | sudo -E bash

WORKDIR /opt

RUN chown www-data:www-data -R /var/www && ln -s /files/entrypoint.sh /usr/local/bin/entrypoint

ENTRYPOINT ["/files/entrypoint.sh"]

CMD ["apache2-foreground"]
