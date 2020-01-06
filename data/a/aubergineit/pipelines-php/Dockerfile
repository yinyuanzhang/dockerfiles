FROM php:7.2-stretch

RUN     docker-php-source extract && \
        umask && \
        umask 0022 && \
        apt-get update && \
    	pecl install igbinary && docker-php-ext-enable igbinary && \
        pecl install mongodb && docker-php-ext-enable mongodb && \
        docker-php-ext-install fileinfo && \
        apt-get -y --no-install-recommends install libzip-dev libicu-dev gnupg libfreetype6-dev libjpeg62-turbo-dev \
            libpng-dev python build-essential fontforge \
            libxslt-dev mariadb-client libpcre3-dev unzip git openssh-client xxd libmagickwand-dev ruby ruby-dev && \
		docker-php-ext-install zip && \
		docker-php-ext-install opcache && \
		docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-php-ext-install -j$(nproc) gd && \
        docker-php-ext-install -j$(nproc) sockets && \
		docker-php-ext-install intl && \
		docker-php-ext-install pdo pdo_mysql && \
		docker-php-ext-install soap && \
		docker-php-ext-install xsl && \
        yes "" | pecl install imagick && docker-php-ext-enable imagick && \
        curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
        curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
        apt-get install -y nodejs libsass-dev node-bindings node-gyp && \
        npm install -g gulp && \
        npm install -g yarn && \
        gem install compass && \
        docker-php-source delete && \
		apt-get clean
