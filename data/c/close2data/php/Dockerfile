FROM php:7.2-fpm-buster

ARG xdebug=1

# Install selected extensions and other stuff
RUN \
    apt-get update && apt-get install -y \
		apt-transport-https \
		apt-utils \
        libfreetype6-dev \
		libjpeg-dev \
		libpng-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libyaml-dev \
        libbz2-dev \
        libicu-dev \
        libxml2-dev \
        libxslt-dev \
        imagemagick \
        libmagickwand-dev \
		zlib1g \
		git \
		gnupg2 \
		unzip \
		libmemcached11 \
        libmemcachedutil2 \
        build-essential \
        libmemcached-dev \
        libz-dev \
        libssh2-1-dev \
        libssh2-1 && \
    apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
        NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
    docker-php-ext-install -j${NPROC} gd iconv mysqli pdo_mysql bcmath bz2 intl mbstring soap xsl zip opcache exif && \
    pecl install redis imagick mcrypt-1.0.1 && \
        docker-php-ext-enable redis imagick mcrypt && \
    git clone https://github.com/php/pecl-networking-ssh2.git /usr/src/php/ext/ssh2 && \
	    docker-php-ext-install ssh2 && \
    apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN \
    pecl install xdebug && \
        docker-php-ext-enable xdebug && \
        echo "xdebug.idekey = PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.default_enable = 1" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_autostart = 1" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_connect_back = 0" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.profiler_enable = 0" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_log='/tmp/xdebug.log'" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_host = 127.0.0.1" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
        echo "xdebug.remote_port = 9000" >> /usr/local/etc/php/conf.d/xdebug.ini.disabled && \
    apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    curl -sS https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" | tee /etc/apt/sources.list.d/postgres.list && \
    apt-get update && apt-get install -y nodejs yarn libpq-dev && \
        docker-php-ext-install -j$(nproc) pdo_pgsql && \
    apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
