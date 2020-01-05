FROM php:7.1.21-fpm
# set mainainer
LABEL maintainer="Grokon"
# add user
RUN adduser --disabled-login --no-create-home --group --uid 3000 --system app
# add php-modules
RUN apt-get update && apt-get install -q -y --no-install-recommends \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libmcrypt-dev \
        libicu-dev \
        libmagickwand-dev \
        libssh2-1-dev \
        libxslt1-dev \
        git \
        locales && \
    docker-php-ext-install -j$(nproc) exif && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) gd && \
    docker-php-ext-install -j$(nproc) gettext && \
    docker-php-ext-configure intl && \
    docker-php-ext-install -j$(nproc) intl && \
    docker-php-ext-install -j$(nproc) mcrypt && \
    docker-php-ext-install -j$(nproc) mysqli && \
    docker-php-ext-configure opcache --enable-opcache && \
    docker-php-ext-install opcache && \
    docker-php-ext-install -j$(nproc) pdo_mysql  && \
    docker-php-ext-install -j$(nproc) pcntl && \
    docker-php-ext-install -j$(nproc) shmop && \
    docker-php-ext-install -j$(nproc) sockets && \
    docker-php-ext-install -j$(nproc) sysvmsg && \
    docker-php-ext-install -j$(nproc) sysvsem && \
    docker-php-ext-install -j$(nproc) sysvshm && \
    docker-php-ext-install -j$(nproc) xsl && \
    docker-php-ext-install -j$(nproc) zip && \
    git clone --depth=1 -q https://github.com/tony2001/pinba_extension.git /usr/src/php/ext/pinba && \
    docker-php-ext-configure pinba --enable-pinba && \
    docker-php-ext-install pinba && \    
    echo "pinba.enabled = 1" >> /usr/local/etc/php/conf.d/docker-php-ext-pinba.ini && \
    echo 'pinba.server = ${PINBA_SERVER}' >> /usr/local/etc/php/conf.d/docker-php-ext-pinba.ini && \
    pecl install redis && \
    pecl install igbinary && \
    pecl install imagick && \
    pecl install ssh2-1.1.2 && \
    docker-php-ext-enable redis igbinary imagick ssh2
# add locale
RUN sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# ro_RO.UTF-8 UTF-8/ro_RO.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# kk_KZ.UTF-8 UTF-8/kk_KZ.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# el_GR.UTF-8 UTF-8/el_GR.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
# add configs
COPY conf/php.ini /usr/local/etc/php/php.ini
COPY conf/www.conf /usr/local/etc/php-fpm.d/www.conf
# add symfony-log
RUN mkdir -p /var/log/symfony-log/ && \
    chown app:app /var/log/symfony-log/
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# set-up port
EXPOSE 9000
# cmd command
CMD ["php-fpm"]