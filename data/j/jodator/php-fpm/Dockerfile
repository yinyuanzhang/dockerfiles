FROM jodator/nginx

MAINTAINER Maciej Gołaszewski <jodator@gmail.com>

RUN \
    apt-get update && \
    apt-get install -y \
        php5-apc \
        php5-cli \
        php5-common \
        php5-curl \
        php5-fpm \
        php5-gd \
        php5-http \
        php5-imagick \
        php5-intl \
        php5-mcrypt \
        php5-memcache \
        php5-mysql \
        php5-tidy

RUN \
    rm -rf /etc/php5/cli/php.ini && \
    ln -s /etc/php5/fpm/php.ini /etc/php5/cli/php.ini

RUN \
    apt-get autoremove && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD etc /etc

ADD supervisord.conf /etc/supervisor/conf.d/php-fpm.conf
