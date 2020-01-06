FROM php:7.2.24-fpm

# Python serve a casperjs
RUN apt-get update && \
    apt-get install -y \
        locales \
        unzip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libcurl4-openssl-dev \
        libc-client2007e-dev \
        libkrb5-dev \
        libicu-dev \
        libxml2-dev \
        libssh2-1-dev \
        libgmp-dev \
        libssl-dev \
        vim \
        python \
        python-pip \
        dumb-init && \
    apt-get autoremove -yf && \
    rm -r /var/lib/apt/lists/* && \
    echo "it_IT.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=it_IT.UTF-8 LANGUAGE=it_IT LC_ALL=it_IT.UTF-8 && \
    export LANG=it_IT.UTF-8 LANGUAGE=it_IT LC_ALL=it_IT.UTF-8 && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \
    docker-php-ext-install -j$(nproc) \
        gd \
        imap \
        curl \
        iconv \
        bcmath \
        gmp \
        ftp \
        intl \
        mbstring \
        pcntl \
        soap \
        sockets \
        opcache \
        shmop \
        calendar \
        pdo_mysql \
        zip && \
    pecl install redis-3.1.6 && \
    docker-php-ext-enable redis && \
    pecl install ssh2-1.1.2 && \
    docker-php-ext-enable ssh2 && \
    curl -o newrelic-php.tar.gz https://download.newrelic.com/php_agent/release/newrelic-php5-9.3.0.248-linux.tar.gz && \
    tar xzvf newrelic-php.tar.gz && \
    mv newrelic-php5-* /opt/newrelic-php && \
    rm newrelic-php.tar.gz && \
    curl -s -o /usr/bin/composer https://getcomposer.org/download/1.9.0/composer.phar && \
    chmod +x /usr/bin/composer && \
    mkdir -p /usr/local/etc/fpm.d /var/log/php-fpm && \
    chown www-data:www-data /var/log/php-fpm && \
    ln -s /usr/local/bin/php /usr/bin && \
    curl -s -L -o ./biscuit-linux_amd64.tgz https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-linux_amd64.tgz && \
    tar xzvf biscuit-linux_amd64.tgz && \
    mv biscuit /usr/bin/biscuit && \
    chmod +x /usr/bin/biscuit && \
    rm biscuit-linux_amd64.tgz && \
    pip install awscli && \
    aws configure set s3.signature_version s3v4

COPY files/php.ini /usr/local/etc/php/php.ini
COPY files/php-fpm.conf /usr/local/etc/php-fpm.conf

# TZ: https://github.com/primait/board/issues/1631
ENV LANG=it_IT.UTF-8 \
    LANGUAGE=it_IT \
    LC_ALL=it_IT.UTF-8 \
    TZ=:/etc/localtime

COPY files/setup_common.sh /setup_common.sh
COPY files/entrypoint.sh /entrypoint.sh
COPY files/decrypt_secrets.sh /decrypt_secrets.sh

WORKDIR /app

ENV PHP_OPCACHE_VALIDATE_TIMESTAMPS=0

ENTRYPOINT ["/usr/bin/dumb-init", "--", "/entrypoint.sh"]
