FROM php:7.3-apache
MAINTAINER dev@chialab.it
ENV DEBIAN_FRONTEND noninteractive
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
    && docker-php-ext-enable memcached.so redis.so \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /var/lib/apt/lists/* \
    && a2enmod headers \
    && a2enmod deflate \
    && a2enmod expires \
    && a2enmod rewrite


# Add crontab file in the cron directory
#ADD crontab /etc/cron.d/import-cron
 
# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/import-cron
 
# Create the log file to be able to run tail
#RUN touch /var/log/import_queue.log

RUN touch /root/project_env.sh

ADD https://fa109fcdb5dfa3e3700ce781870512702d6815a6:x-oauth-basic@api.github.com/repos/rolandihms/ihmsT-php-admin/compare/master...HEAD /dev/null

#https://api.github.com/repos/rolandihms/ihmsT-php-admin/git/refs/heads/master version.json

#ADD https://api.github.com/repos/docker/docker/compare/master...HEAD /dev/nul

# Clone our private GitHub Repository
RUN git clone -b master https://fa109fcdb5dfa3e3700ce781870512702d6815a6:x-oauth-basic@github.com/rolandihms/ihmsT-php-admin.git /myapp/

RUN cp -R /myapp/* /var/www/

WORKDIR /var/www

#add .htaccess tmp for mods
#COPY .htaccess_tmpl /var/www/.htaccess

COPY .docker/php/vhost.conf /etc/apache2/sites-available/000-default.conf

#Copy PHP custom INI file 
COPY timezone.ini /usr/local/etc/php/conf.d/cust_timezone.ini

#Copy supervisor conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY env_var.sh /var/www/env_var.sh


RUN chmod -R 0777 application/session && chmod -R 0777 assets && chmod -R 0644 /root/project_env.sh
RUN chmod -R 0777 application/logs/

RUN chown www-data:www-data /var/www
RUN chown www-data:www-data /var/www/cron.sh && chmod u+x /var/www/cron.sh && chmod 0777 entrypoint.sh
RUN mkdir -p /var/www/bin 
RUN chmod -R 0777 /var/www/bin
RUN chmod -R 0777 /var/www/application/logs/

#CMD ["env | grep _ >> /etc/environment"]

RUN ["chmod", "+x", "/var/www/env_var.sh"]


# Install Composer.
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && ln -s $(composer config --global home) /root/composer
ENV PATH $PATH:/root/composer/vendor/bin

# Install app dependencies
RUN /usr/local/bin/composer install --no-interaction 
ENV DEBIAN_FRONTEND teletype

#ENTRYPOINT ["/var/www/env_var.sh"]