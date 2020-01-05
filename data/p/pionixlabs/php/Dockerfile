FROM ubuntu:14.04

ENV GOSU_VERSION 1.11
ENV PHP_UID 501
ENV PHP_GID 20
ENV PHP_HOME /home/php
ENV PHP_WORKDIR /usr/share/nginx/html

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gettext \
        unzip \
        libpcre3-dev \
        openssl \
        git-core \
        language-pack-en-base \
        openssh-client \
        software-properties-common \
        gcc \
        make \
        nmap \
        net-tools \
        iputils-ping \
        wget \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    # && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    # && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/php \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        php5 \
        php5-cli \
        php5-fpm \
        php5-mysql \
        php5-curl \
        php5-dev \
        php5-intl \
        php5-json \
        php5-mcrypt \
    && php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/php

# Configure PHP
RUN set -x \
    && sed -i 's/user\ =\ www-data/user\ =\ php/g' /etc/php5/fpm/pool.d/www.conf \
    && sed -i 's/group\ =\ www-data/group\ =\ php/g' /etc/php5/fpm/pool.d/www.conf \
    && sed -i 's/listen.owner\ =\ www-data/listen.owner\ =\ php/g' /etc/php5/fpm/pool.d/www.conf \
    && sed -i 's/listen.group\ =\ www-data/listen.group\ =\ php/g' /etc/php5/fpm/pool.d/www.conf \
    && sed -i 's/listen\ =\ \/var\/run\/php5-fpm\.sock/listen\ =\ 9000/g' /etc/php5/fpm/pool.d/www.conf \
    && sed -i 's/;daemonize\ =\ yes/daemonize\ =\ no/g' /etc/php5/fpm/php-fpm.conf

RUN ln -s /usr/bin/php5 /bin/php \
 && ln -s /usr/bin/php-config5 /bin/php-config \
 && ln -s /usr/bin/phpize5 /bin/phpize \
 && cd / \
 && git clone -b phalcon-v1.3.4 https://github.com/phalcon/cphalcon.git \
 && cd /cphalcon/build \
 && ./install \
 && cd /etc/php5/mods-available \
 && touch phalcon.ini \
 && echo "; configuration for PHALCON module" >> phalcon.ini \
 && echo "; priority=10" >> phalcon.ini \
 && echo "extension=phalcon.so" >> phalcon.ini \
 && ln -s /etc/php5/mods-available/phalcon.ini /etc/php5/cli/conf.d/20-phalcon.ini \
 && ln -s /etc/php5/mods-available/phalcon.ini /etc/php5/fpm/conf.d/20-phalcon.ini

COPY ./entrypoint.sh /opt/php-setup/docker-entrypoint.sh
RUN set -x && chmod +x /opt/php-setup/docker-entrypoint.sh
ENTRYPOINT ["/opt/php-setup/docker-entrypoint.sh"]

EXPOSE 9000
EXPOSE 9111
CMD ["/usr/sbin/php5-fpm"]
