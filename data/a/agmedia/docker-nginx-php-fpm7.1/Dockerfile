FROM ubuntu:16.04

MAINTAINER Danil Kopylov <lobsterk@yandex.ru>

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils \
    software-properties-common \
    python-software-properties \
    language-pack-en-base && \

    LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \

    apt-get update && apt-get upgrade -y && \

    apt-get install -y python-setuptools \
    nginx \
    git \
    curl \
    zip \
    unzip \
    php7.1-fpm \
    ca-certificates \
    gettext \
    mc \
    libmcrypt-dev  \
    libicu-dev \
    libcurl4-openssl-dev \
    mysql-client \
    libldap2-dev \
    libfreetype6-dev \
    libfreetype6 \
    libpng12-dev


# exts
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    php7.1-mongodb \
    php7.1-curl \
    php7.1-cli \
    php7.1-intl \
    php7.1-soap \
    php7.1-xml \
    php7.1-mcrypt \
    php7.1-bcmath \
    php7.1-mysql \
    php7.1-mysqli \
    php7.1-amqp \
    php7.1-mbstring \
    php7.1-ldap \
    php7.1-zip \
    php7.1-iconv \
    php7.1-pgsql \
    php7.1-pdo \
    php7.1-json \
    php7.1-simplexml \
    php7.1-xmlrpc \
    php7.1-gmp \
    php7.1-fileinfo \
    php7.1-sockets \
    php7.1-ldap \
    php7.1-gd \
    php7.1-xdebug && \
    echo "extension=amqp.so" > /etc/php/7.1/fpm/conf.d/10-amqp.ini && \
    rm -f /etc/php/7.1/mods-available/xdebug.ini

RUN curl -sS https://getcomposer.org/installer | php \
        && mv composer.phar /usr/local/bin/ \
        && ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Install node.js
RUN apt-get install -y --no-install-recommends --no-install-suggests \
    nodejs \
    npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g gulp-cli

RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install mail server
COPY mailserver.sh /tmp/mailserver.sh
RUN /tmp/mailserver.sh

# set timezone Europe/Moscow
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& ln -sf /dev/stderr /var/log/php7.1-fpm.log

RUN rm -f /etc/nginx/sites-enabled/*
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
#COPY php.ini /etc/php/7.1/fpm/php.ini


RUN mkdir -p /run/php && touch /run/php/php7.1-fpm.sock && touch /run/php/php7.1-fpm.pid
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
EXPOSE 80
CMD ["/entrypoint.sh"]
