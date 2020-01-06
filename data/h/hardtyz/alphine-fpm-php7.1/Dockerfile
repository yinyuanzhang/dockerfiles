# PHP Docker image for Yii 2.0 Framework runtime
# ==============================================

ARG PHP_BASE_IMAGE_VERSION
FROM php:7.1-fpm-alpine

# Install system packages & PHP extensions required for Yii 2.0 Framework
RUN apk --update --virtual build-deps add --no-cache \
        autoconf \
        make \
        gcc \
        g++ \
        libtool \
        icu-dev \
        curl-dev \
        freetype-dev \
        libmcrypt-dev \
        imagemagick-dev \
        pcre-dev \
        postgresql-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        libxml2-dev && \
     apk add --no-cache \
        nginx \
        git \
        curl \
        bash \
        bash-completion \
        icu \
        sed \
        re2c \
        m4 \
        imagemagick \
        pcre \
        freetype \
        libintl \
        ca-certificates \
        libjpeg-turbo \
        libpng \
        libmcrypt \
        libltdl \
        libxml2 \
        supervisor \
        zlib \
        libressl \
        pcre \
        py-pip  \
        mysql-client \
        postgresql && \
    mkdir -p /usr/lib/php/ && \
    ln -s  /usr/local/lib/php/extensions/no-debug-non-zts-20160303 /usr/lib/php/modules && \
    docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-configure bcmath && \
    docker-php-ext-configure soap && \
    docker-php-ext-configure mcrypt --with-mcrypt && \
    docker-php-ext-install \
        mcrypt \
        soap \
        zip \
        curl \
        bcmath \
        exif \
        gd \
        iconv \
        intl \
        mbstring \
        opcache \
        pdo_mysql \
        pdo_pgsql && \
        pecl install \
        imagick \
        mongodb && \
    pecl install -f xdebug && \
    docker-php-ext-enable xdebug && \
    apk del \
        build-deps && \
    rm -rf /var/cache/apk/* 

RUN echo "extension=imagick.so" > /usr/local/etc/php/conf.d/pecl-imagick.ini && \
    echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/pecl-mongodb.ini && \
    echo "error_reporting = E_ALL & ~E_DEPRECATED" >> /usr/local/etc/php/conf.d/base.ini

RUN mkdir -p /run/nginx/ && \
    chmod ugo+w /run/nginx/ && \
    rm -f /etc/nginx/nginx.conf && \
    mkdir -p /etc/nginx/conf.d && \
    mkdir -p /etc/nginx/ssl/ && \
    mkdir -p /var/www/html/ && \
    chmod -R 775 /var/www/ && \
    chown -R nginx:nginx /var/www/ && \
    pip install --upgrade pip && \
    pip install supervisor-stdout

# Configure version constraints
ENV PHP_ENABLE_XDEBUG=0 \
    PATH=/app:/app/vendor/bin:/root/.composer/vendor/bin:$PATH \
    TERM=linux \
    VERSION_PRESTISSIMO_PLUGIN=^0.3.7 \
    COMPOSER_ALLOW_SUPERUSER=1
    
# Add configuration files
COPY image-files/ /

#Install ioncube loader
RUN  wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz && \
        tar -xzvf ioncube_loaders_lin_x86-64.tar.gz && \
        rm -rf ioncube_loaders_lin_x86-64.tar.gz && \
        export extension_dir=$("php" -r "echo ini_get('extension_dir');") && \
        cp ioncube/ioncube_loader_lin_7.1.so $extension_dir && \
        rm -rf ioncube && \
        echo -e "\nerror_reporting = E_ALL & ~E_DEPRECATED" >> /usr/local/etc/php/conf.d/base.ini && \
        echo 'zend_extension = "'$extension_dir'/ioncube_loader_lin_7.1.so"' >> /usr/local/etc/php/conf.d/base.ini

# Add GITHUB_API_TOKEN support for composer
RUN chmod 700 \
        /usr/local/bin/docker-php-entrypoint \
        /usr/local/bin/composer

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- \
        --filename=composer.phar \
        --install-dir=/usr/local/bin && \
    composer clear-cache

# Install composer plugins
RUN composer global require --optimize-autoloader \
        "hirak/prestissimo:${VERSION_PRESTISSIMO_PLUGIN}" && \
    composer global dumpautoload --optimize && \
    composer clear-cache 

# Application environment
WORKDIR /app
