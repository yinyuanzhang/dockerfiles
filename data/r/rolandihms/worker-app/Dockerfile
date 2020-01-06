FROM php:7.2-apache
MAINTAINER dev@chialab.it

# Install PHP extensions and PECL modules.
RUN buildDeps=" \
        default-libmysqlclient-dev \
        libbz2-dev \
        libmemcached-dev \
        libsasl2-dev \
    " \
    runtimeDeps=" \
        curl \
        git \
        bash \
        libfreetype6-dev \
        libicu-dev \
        libjpeg-dev \
        libldap2-dev \
        libmemcachedutil2 \
        libpng-dev \
        libpq-dev \
        libxml2-dev \
        libzip-dev \
    " \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y $buildDeps $runtimeDeps \
    && docker-php-ext-install bcmath bz2 calendar iconv intl mbstring mysqli opcache pdo_mysql pdo_pgsql pgsql soap zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install ldap \
    && apt-get -y install cron \
    && apt-get -y install supervisor \
    && apt-get -y install nano \
    && apt-get -y install libfontconfig \
    && docker-php-ext-install exif \
    && pecl install memcached redis \
    && pecl install xdebug-2.7.2 \
    && docker-php-ext-enable xdebug \
    && docker-php-ext-enable memcached.so redis.so \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /var/lib/apt/lists/* \
    && a2enmod headers \
    && a2enmod deflate \
    && a2enmod expires \
    && a2enmod rewrite


# Add crontab file in the cron directory
ADD crontab /etc/cron.d/import-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/import-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/import_queue.log
RUN touch /var/log/db_backup.log
RUN touch /var/log/email_queue.log

RUN touch /root/project_env.sh

COPY .docker/php/vhost.conf /etc/apache2/sites-available/000-default.conf

ADD https://fa109fcdb5dfa3e3700ce781870512702d6815a6:x-oauth-basic@api.github.com/repos/rolandihms/ihmsT-php-admin/compare/master...HEAD /dev/null


# Clone our private GitHub Repository
RUN mkdir /myapp
RUN git clone -b master https://fa109fcdb5dfa3e3700ce781870512702d6815a6:x-oauth-basic@github.com/rolandihms/ihmsT-php-admin.git /myapp/
RUN mv /myapp/* /var/www/

WORKDIR /var/www


#Copy PHP custom INI file 
COPY timezone.ini /usr/local/etc/php/conf.d/cust_timezone.ini

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /var/www/entrypoint.sh

RUN chmod -R 0777 application/session && chmod -R 0644 /root/project_env.sh

RUN chown www-data:www-data /var/www
RUN chown root:root /etc/cron.d/import-cron
RUN chown root:root /var/www/cron.sh && chmod u+x /var/www/cron.sh
RUN chown root:root /var/www/entrypoint.sh && chmod u+x /var/www/entrypoint.sh

RUN mkdir /var/www/bin 
RUN chmod -R 0777 /var/www/bin
RUN chmod -R 0777 /var/www/application/logs/

RUN ["chmod", "+x", "/var/www/entrypoint.sh"]

CMD ["env | grep _ >> /etc/environment"]

# Apply cron job
RUN crontab /etc/cron.d/import-cron

# Install Composer.
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && ln -s $(composer config --global home) /root/composer
ENV PATH $PATH:/root/composer/vendor/bin

# Install app dependencies
RUN /usr/local/bin/composer install --no-interaction 

#run supervisor
#CMD ["/usr/bin/supervisord"]
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
ENTRYPOINT ["sh","/var/www/entrypoint.sh"]