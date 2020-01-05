###
# MeuPatrocinio
#
# Repository:    PHP
# Image:         CLI/Base
# Version:       7.2.x
# Strategy:      PHP From PHP-Alpine Repository + curl with http2 support
# Base distro:   Alpine 3.10
#
FROM alpine:3.10

# Variables for enabling NewRelic
ENV NR_ENABLED=false \
    NR_APP_NAME="" \
    NR_LICENSE_KEY="" \
    TERM=xterm-256color \
    COLORTERM=truecolor \
    COMPOSER_PROCESS_TIMEOUT=1200

# Add the ENTRYPOINT script
ADD wait-for-file.sh /scripts/wait-for-file.sh
ADD start.sh /scripts/start.sh
ADD bashrc /root/.bashrc

#Install openssh
RUN apk add --no-cache openssh
VOLUME /root/.ssh

# Install PHP From DotDeb, Common Extensions, Composer and then cleanup
RUN echo "---> Enabling PHP-Alpine" && \
    apk add --update --no-cache \
    bash \
    openrc \
    curl \
    fontconfig \
    libxrender \
    libxext \
    vim \
    git \
    unzip \
    wget \
    sudo \
    php7 \
    php7-apcu \
    php7-bcmath \
    php7-bz2 \
    php7-ctype \
    php7-curl \
    php7-exif \
    php7-fileinfo \
    php7-fpm \
    php7-gd \
    php7-gmp \
    php7-iconv \
    php7-imagick \
    php7-imap \
    php7-intl \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqlnd \
    php7-opcache \
    php7-openssl \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    php7-pdo_sqlite \
    php7-pgsql \
    php7-phar \
    php7-posix     \
    php7-redis \
    php7-simplexml \
    php7-soap \
    php7-sqlite3 \
    php7-tokenizer \
    php7-xdebug \
    php7-xml \
    php7-xmlreader \
    php7-xmlwriter \
    php7-xsl \
    php7-zip \
    php7-zlib \
    php7-phpdbg && \
    echo "---> Installing Composer" && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    mkdir -p /var/www/app && \
    wget -O /tini https://github.com/krallin/tini/releases/download/v0.18.0/tini-static && \
    chmod +x /tini && \
    echo "---> Configuring PHP" && \
    sed -i "/listen = .*/c\listen = [::]:9000" /etc/php7/php-fpm.d/www.conf && \
    sed -i "/;access.log = .*/c\access.log = /proc/self/fd/2" /etc/php7/php-fpm.d/www.conf && \
    sed -i "/;clear_env = .*/c\clear_env = no" /etc/php7/php-fpm.d/www.conf && \
    sed -i "/;catch_workers_output = .*/c\catch_workers_output = yes" /etc/php7/php-fpm.d/www.conf && \
    sed -i "/pid = .*/c\;pid = /run/php/php7.1-fpm.pid" /etc/php7/php-fpm.conf && \
    sed -i "/;daemonize = .*/c\daemonize = yes" /etc/php7/php-fpm.conf && \
    sed -i "/error_log = .*/c\error_log = /proc/self/fd/2" /etc/php7/php-fpm.conf && \
    sed -i "/post_max_size = .*/c\post_max_size = 1000M" /etc/php7/php.ini && \
    sed -i "/memory_limit = .*/c\memory_limit = 4096M" /etc/php7/php.ini && \
    sed -i "/upload_max_filesize = .*/c\upload_max_filesize = 1000M" /etc/php7/php.ini && \
    echo "---> Adding Support for NewRelic" && \
    mkdir /etc/newrelic && \
    mkdir /tmp/newrelic && \
    cd /tmp/newrelic && \
    wget -r -l1 -nd -A"linux-musl.tar.gz" https://download.newrelic.com/php_agent/release/ && \
    gzip -dc newrelic*.tar.gz | tar xf - && \
    cd newrelic-php5* && \
    rm -f /usr/lib/php7/modules/newrelic.so && \
    cp ./agent/x64/newrelic-20180731.so /usr/lib/php7/modules/newrelic.so && \
    cp ./daemon/newrelic-daemon.x64 /usr/bin/newrelic-daemon && \
    cp ./scripts/init.alpine /etc/init.d/newrelic-daemon && \
    cp ./scripts/newrelic.ini.template /scripts/newrelic.ini && \
    cp ./scripts/newrelic.cfg.template /etc/newrelic/newrelic.cfg && \
    sed -i -r 's/;newrelic.distributed_tracing_enabled = false/newrelic.distributed_tracing_enabled = true/' /scripts/newrelic.ini && \ 
    mkdir /var/log/newrelic && \
    chmod +x /scripts/*.sh && \
    chmod +x /etc/init.d/newrelic-daemon

# Curl + Http2
ENV CURL_VERSION 7.60.0

RUN apk add --update --no-cache openssl openssl-dev nghttp2-dev ca-certificates
RUN apk add --update --no-cache --virtual curldeps g++ make perl && \
    wget https://curl.haxx.se/download/curl-$CURL_VERSION.tar.bz2 && \
    tar xjvf curl-$CURL_VERSION.tar.bz2 && \
    rm curl-$CURL_VERSION.tar.bz2 && \
    cd curl-$CURL_VERSION && \
    ./configure \
        --with-nghttp2=/usr \
        --prefix=/usr \
        --with-ssl \
        --enable-ipv6 \
        --enable-unix-sockets \
        --without-libidn \
        --disable-static \
        --disable-ldap \
        --with-pic && \
    make && \
    make install && \
    cd / && \
    echo "---> Cleaning up" && \
    #rm -rf /tmp && \
    rm -r curl-$CURL_VERSION && \
    rm -r /var/cache/apk && \
    rm -r /usr/share/man && \
    apk del curldeps

# Application directory
WORKDIR "/var/www/app"

# Environment variables
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Define the entry point that tries to enable newrelic
ENTRYPOINT ["/tini", "--", "/scripts/start.sh"]

# As non daemon and single base image, it may be used as cli container
CMD ["/bin/bash"]