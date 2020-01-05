FROM dezinger/ubuntu-18:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive
ENV SSH_KEYS_DIRECTORY /root/.ssh
ARG PHP_VERSION=7.3
ENV PHP_VERSION=${PHP_VERSION}

COPY files/ /
WORKDIR /var/www

RUN \
# add repo php5.6/7 & apache2
    apt-get -y update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:ondrej/apache2 && \
    add-apt-repository ppa:ondrej/php && \
# setup
    apt-get -y update && \
    apt-get install --no-install-recommends -y \
    ssh ca-certificates git openjdk-8-jdk \
    apache2 libreoffice unoconv \
    libapache2-mod-rpaf \
    libapache2-mod-php$PHP_VERSION \
    php$PHP_VERSION-cli \
    php$PHP_VERSION-pgsql \
    php$PHP_VERSION-curl \
    php$PHP_VERSION-common \
    php$PHP_VERSION-gd \
    php$PHP_VERSION-xsl \
    php$PHP_VERSION-xmlrpc \
    php$PHP_VERSION-tidy \
    libmemcached-dev \
    php$PHP_VERSION-memcached \
    imagemagick \
    php$PHP_VERSION-imagick \
    php$PHP_VERSION-intl \
    php$PHP_VERSION-mbstring \
    php$PHP_VERSION-msgpack \
    php$PHP_VERSION-zip \
    php$PHP_VERSION-soap \
    php$PHP_VERSION-bcmath \
    php-pear \
    php$PHP_VERSION-dev \
    libmcrypt4 \
    libmcrypt-dev \
    make \
    zlib1g-dev && \
    pecl install mcrypt-1.0.2 && \
# config php & ext
    ln -sf /etc/php/$PHP_VERSION/cli/php.ini /etc/php/$PHP_VERSION/apache2/php.ini && \
    ln -sf /etc/php/$PHP_VERSION/mods-available/mcrypt.ini /etc/php/$PHP_VERSION/apache2/conf.d/20-mcrypt.ini && \
    ln -sf /etc/php/$PHP_VERSION/mods-available/mcrypt.ini /etc/php/$PHP_VERSION/cli/conf.d/20-mcrypt.ini && \
# print version & modules
    php -v && \
    php -m && \
# enabled apache2 modules
    a2enmod headers rewrite remoteip && \
# setup composer
    php -r "readfile('http://getcomposer.org/installer');" | \
    php -- --install-dir=/usr/local/bin/ --filename=composer && \
    chmod a+x /usr/local/bin/composer && \
# setup mode
    chmod a+x /usr/local/bin/add-ssh-keys.sh && \
    chmod a+x /etc/init.d/libreoffice && \
# clean
    apt-get remove -y software-properties-common && \
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm /var/log/lastlog /var/log/faillog && \
# user
    usermod -u 1000 www-data

VOLUME ["$SSH_KEYS_DIRECTORY", "/var/www"]

EXPOSE 8080