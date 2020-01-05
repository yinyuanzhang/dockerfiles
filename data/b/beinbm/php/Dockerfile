FROM debian:buster-slim
MAINTAINER Marco Beinbrech <marco@beinbrech.com>

### INSTALL APACHE & PHP
RUN apt-get update && apt-get install -y \
        apache2 \
        curl \
        gnupg \
        libapache2-mod-php7.2 \
        php7.2 \
        php7.2-bcmath \
        php7.2-curl \
        php7.2-gmp \
        php7.2-gd \
        php7.2-intl \
        php7.2-mysql \
        php7.2-mbstring \
        php7.2-sqlite3 \
        php7.2-xml \
        php-xdebug \
        unzip \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr /var/log/apache2/error.log
RUN a2enmod rewrite
RUN usermod -u 1000 www-data

# https://getcomposer.org/doc/03-cli.md#composer-allow-superuser
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

### SETUP CONTAINER
RUN { \
        echo '<VirtualHost *:80>'; \
        echo '	DocumentRoot /var/www/html/public'; \
        echo ; \
        echo '	LogLevel info'; \
        echo '	ErrorLog ${APACHE_LOG_DIR}/error.log'; \
        echo '	CustomLog ${APACHE_LOG_DIR}/access.log combined'; \
        echo ; \
        echo '	<Directory /var/www>'; \
        echo '		Options Indexes FollowSymLinks'; \
        echo '		AllowOverride all'; \
        echo '		Require all granted'; \
        echo '	</Directory>'; \
        echo ; \
        echo '</VirtualHost>'; \
    } > /etc/apache2/sites-available/000-default.conf

RUN { \
        echo '[PHP]'; \
        echo 'max_execution_time = 60'; \
        echo 'max_input_time = 60'; \
        echo 'memory_limit = 512M'; \
        echo 'error_reporting = E_ALL & ~E_DEPRECATED'; \
        echo 'variables_order = "GPCS"'; \
        echo 'request_order = "GP"'; \
        echo 'post_max_size = 100M'; \
        echo 'upload_max_filesize = 100M'; \
        echo 'max_file_uploads = 50'; \
        echo 'log_errors = On'; \
        echo 'error_log = /dev/stderr'; \
        echo ''; \
        echo '[Date]'; \
        echo 'date.timezone = Europe/Berlin'; \
    } > /etc/php/zzz-settings.ini

RUN ln -s /etc/php/zzz-settings.ini /etc/php/7.2/apache2/conf.d/zzz-settings.ini
RUN ln -s /etc/php/zzz-settings.ini /etc/php/7.2/cli/conf.d/zzz-settings.ini
RUN echo "\nxdebug.remote_enable=on\nxdebug.remote_autostart=on" >> /etc/php/7.2/mods-available/xdebug.ini

EXPOSE 80
WORKDIR /var/www/html
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
