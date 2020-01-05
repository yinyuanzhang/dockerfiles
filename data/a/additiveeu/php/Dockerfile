FROM php:5.6-cli

ENV XDEBUG_COVERAGE_ENABLE false
ENV XDEBUG_REMOTE_ENABLE false
ENV XDEBUG_REMOTE_AUTOSTART true
ENV XDEBUG_REMOTE_PORT 9000
ENV XDEBUG_REMOTE_HOST 172.17.0.1

RUN apt-get update && \
    apt-get install -y git \
                       curl \
                       unzip \
                       openssh-client \
                       libmagickwand-dev \
                       libmagickwand-6.q16-3 \
                       libmcrypt-dev \
                       libssl-dev \
                       libicu-dev libxslt1-dev \
                       zlib1g-dev \
                    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-source extract && \
    pecl install mongo imagick xdebug-2.5.0 && \
    docker-php-ext-enable mongo imagick xdebug && \
    docker-php-ext-install mbstring \
                           xml \
                           intl \
                           mcrypt \
                           pcntl \
                           zip && \
    docker-php-source delete && \
    # Composer
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/bin/composer && \
    /usr/bin/composer global require hirak/prestissimo && \
    apt-get purge -y --auto-remove \
                  -o APT::AutoRemove::RecommendsImportant=false \
                  libssl-dev \
                  libicu-dev \
                  libxslt1-dev \
                  libmagickwand-dev \
                  zlib1g-dev

RUN echo 'xdebug.remote_autostart=${XDEBUG_REMOTE_AUTOSTART}' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini && \
    echo 'xdebug.coverage_enable=${XDEBUG_COVERAGE_ENABLE}' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini && \
    echo 'xdebug.remote_enable=${XDEBUG_REMOTE_ENABLE}' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini && \
    echo 'xdebug.remote_port=${XDEBUG_REMOTE_PORT}' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini && \
    echo 'xdebug.remote_host=${XDEBUG_REMOTE_HOST}' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini && \
    echo 'xdebug.overload_var_dump=0' >> $PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini
