FROM drupal:7

ENV MEMCACHED_HOST memcached
ENV SITEROOT /var/www/html

# Upgrade to latest version of Apache to enable http2 module
RUN cp /etc/apache2/envvars ~/envvars
RUN sed -i 's/jessie/stretch/g' /etc/apt/sources.list
RUN apt-get update
RUN echo "y" | apt-get install -y apache2
RUN rm /etc/apache2/envvars && mv ~/envvars /etc/apache2/envvars
RUN a2enmod http2
RUN sed -i 's/stretch/jessie/g' /etc/apt/sources.list

# Install memcached PHP extension
RUN apt-get update && apt-get install -y libmemcached-dev libmemcached11 build-essential zlib1g-dev unzip || true && \
    export PHP_EXT_DIR=/usr/src/php/ext && mkdir -p /usr/src/php/ext/memcached || true && \
    curl -O https://codeload.github.com/php-memcached-dev/php-memcached/zip/php7 && unzip php7 && mv php-memcached-php7/* /usr/src/php/ext/memcached && mv php-memcached-php7/.* /usr/src/php/ext/memcached || true && \
    rm php7 && rm -rf php-memcached-php7 && docker-php-ext-install memcached  
RUN pecl install jsmin || true && exit 0
RUN cp -R /usr/local/include/php/ext/jsmin /usr/src/php/ext/jsmin
RUN echo "extension=jsmin.so" > /usr/local/etc/php/conf.d/ext-jsmin.ini
    
COPY config/php.ini /usr/local/etc/php/
COPY config/docker-php-ext-memcached.ini /usr/local/etc/php/conf.d/
COPY config/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY config/000-default-no-auth.conf ~/000-default-no-auth.conf
RUN chown root:staff /usr/local/etc/php/php.ini /usr/local/etc/php/conf.d/docker-php-ext-memcached.ini

# Work-around for having code wiped out when mounted to host volume
RUN mkdir /var/www/code && mv ${SITEROOT}/* /var/www/code && mv ${SITEROOT}/.* /var/www/code || true && exit 0
  
ADD start.sh /start.sh
RUN chmod 777 /start.sh
CMD ["/start.sh"]
