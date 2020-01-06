FROM ubuntu:18.04

# APT Packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y && \
    apt-get install -y \
        apt-utils \
        nginx \
        supervisor \
        curl \
        fail2ban \
        unzip \
        apache2-utils \
        locales \
        mysql-client \
        iputils-ping \
        nano \
        php7.2 \
        php7.2-curl \
        php7.2-cli \
        php7.2-gd \
        php7.2-json \
        php7.2-mysql \
        php7.2-cgi \
        php7.2-fpm \
        php7.2-xsl \
        php7.2-soap \
        php7.2-imap \
        php7.2-gmp \
        php7.2-mbstring \
        php7.2-zip \
        php7.2-intl \
        php-imagick \
        && \
    rm -rf /var/lib/apt/lists/*

# Update locale
RUN locale-gen --purge en_US en_US.UTF-8 en_GB.UTF-8 nb_NO.UTF-8 && \
    update-locale "LANG=en_GB.UTF-8 LANGUAGE=en_GB.UTF-8 LC_CTYPE=en_GB.UTF-8 LC_TIME=nb_NO.UTF-8 LC_TELEPHONE=nb_NO.UTF-8 LC_MEASUREMENT=nb_NO.UTF-8" && \
    ln -sf /usr/share/zoneinfo/Europe/Oslo /etc/localtime

# Make directories
RUN mkdir -p /var/log/supervisor && mkdir -p /run/php

#Set log settings for nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy Supervisor config
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy PHP pool config
COPY ./www.conf /etc/php/7.2/fpm/pool.d/www.conf
# Copy php.ini config
COPY ./php.ini /etc/php/7.2/fpm/php.ini

# Add a default nginx config for quick webhost setups
COPY ./nginx_default.conf /etc/nginx/conf.d/default.conf

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

# Expose HTTP port
EXPOSE 80

# Expose HTTPS port
EXPOSE 443