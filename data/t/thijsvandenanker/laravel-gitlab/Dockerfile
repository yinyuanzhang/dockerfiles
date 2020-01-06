FROM php:7.1
MAINTAINER Thijs van den Anker <thijs@bitsnbolts.nl>

RUN apt-get update && apt-get install -y \
	    git \
	    libcurl4-gnutls-dev \
	    libicu-dev \
	    libmcrypt-dev \
	    libvpx-dev \
	    libjpeg-dev \
	    libpng-dev \
	    libxpm-dev \
	    zlib1g-dev \
	    libfreetype6-dev \
	    libxml2-dev \
	    libexpat1-dev \
	    libbz2-dev \
	    libgmp3-dev \
	    libldap2-dev \
	    unixodbc-dev \
	    libpq-dev \
	    libsqlite3-dev \
	    libaspell-dev \
	    libsnmp-dev \
	    libpcre3-dev \
	    libtidy-dev \
	    software-properties-common \
	    zip unzip\
	    ntfs-3g\
	    cifs-utils\
	    gnupg\
    && docker-php-ext-install mbstring mcrypt pdo_mysql curl json intl gd xml zip bz2 opcache soap tidy bcmath \
    && cd ~ \
    && curl -O https://raw.githubusercontent.com/laravel/laravel/master/composer.json \
    && curl -sS https://getcomposer.org/installer | php \
    && php composer.phar install --no-autoloader --no-scripts --no-suggest \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install nodejs -y \
    && npm i -g cross-env \
    && pear install PHP_CodeSniffer

