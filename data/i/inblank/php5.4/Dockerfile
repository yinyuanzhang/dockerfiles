FROM php:5.4-apache
RUN apt-get update && apt-get install -y \
        libapache2-mod-rpaf \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libicu-dev \
    && a2enmod rewrite rpaf \
    && docker-php-ext-install pdo_mysql mysql mcrypt intl mbstring \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
RUN apt-get install -y \
        libmemcached-dev \
    && curl -fsSL 'https://github.com/php-memcached-dev/php-memcached/archive/2.2.0.tar.gz' -o memcached.tar.gz \
    && mkdir -p memcached \
    && tar -xf memcached.tar.gz -C memcached --strip-components=1 \
    && rm memcached.tar.gz \
    && ( \
        cd memcached \
        && phpize \
        && ./configure --enable-memcached \
        && make -j$(nproc) \
        && make install \
    ) \
    && rm -r memcached \
    && docker-php-ext-enable memcached
RUN apt-get install -y \
      exim4 \
    && useradd -G sudo -p $(perl -e'print crypt("tester", "tester")') -m -s /bin/bash -N tester \
    && echo "sendmail_path = /usr/sbin/sendmail -t -i" > /usr/local/etc/php/php.ini
