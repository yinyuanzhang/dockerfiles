FROM php:7.2-apache
CMD apache2-foreground
COPY base-apache.conf /etc/apache2/conf-enabled/base.conf
HEALTHCHECK CMD curl -f http://localhost/ || exit 1
WORKDIR /var/www
RUN ln -sf /dev/stdout /var/log/apache2/access.log \
    && ln -sf /dev/stderr /var/log/apache2/error.log \
    && adduser www-data root
RUN apt-get update \
    && apt-get upgrade --yes \
    && apt-get install --yes apt-utils libgd-dev libgmp-dev \
        libgmp3-dev libmcrypt-dev libpng-dev libssl-dev mysql-client \
    && ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \
    && docker-php-ext-configure gmp --with-gmp=/usr/include/x86_64-linux-gnu \
    && docker-php-ext-install -j$(nproc) gd gmp pdo pdo_mysql
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN pear install Mail \
    && pear install Mail_mime \
    && pear install Net_SMTP
