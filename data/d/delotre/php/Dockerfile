from php:7.3-fpm
MAINTAINER DELOTRE <dsi@delotre.com>

# =========================================
# Install common tools and .bashrc file
# =========================================
ADD docker-generics/* /docker-generics/
RUN cp /docker-generics/bashrc.root /root/.bashrc
RUN bash /docker-generics/apt.sh


RUN apt-get install -y --no-install-recommends \
		libzip-dev \
		libjpeg-dev \
        libpng-dev

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
    docker-php-ext-install gd mysqli opcache zip;

RUN { \
	echo 'opcache.memory_consumption=128'; \
	echo 'opcache.interned_strings_buffer=8'; \
	echo 'opcache.max_accelerated_files=12000'; \
	echo 'opcache.revalidate_freq=2'; \
	echo 'opcache.fast_shutdown=1'; \
	echo 'opcache.enable_cli=1'; \
} > /usr/local/etc/php/conf.d/opcache.ini; \
{ \
	echo 'php_flag[display_errors] = on'; \
	echo 'php_admin_value[error_log] = /var/log/fpm-php.www.log'; \
	echo 'php_admin_flag[log_errors] = on'; \
	echo 'php_admin_value[memory_limit] = 128M'; \
} > /usr/local/etc/php-fpm.d/errors.conf; \
{ \
	echo 'memory_limit = __PHP_MEMORY_LIMIT__; Variable: PHP_MEMORY_LIMIT'; \
	echo 'post_max_size = __UPLOAD_MAX_FILESIZE__; Variable UPLOAD_MAX_FILESIZE'; \
	echo 'upload_max_filesize = __UPLOAD_MAX_FILESIZE__; Variable UPLOAD_MAX_FILESIZE'; \
	echo 'sendmail_path = /usr/sbin/ssmtp -t'; \
} > /usr/local/etc/php/conf.d/local.ini

ADD opcache-gui/index.php /var/www/html/opc.php
RUN echo "<?php phpinfo();" > /var/www/html/info.php

# =========================================
# Set ENV variables
# =========================================
ENV DEBUG false
ENV PROJECT_ROOT /var/www/htdocs
ENV FPM_USERNAME=www-data
ENV FPM_UID=33
ENV PHP_MEMORY_LIMIT=128M
ENV UPLOAD_MAX_FILESIZE=100M
ENV PHP_XDEBUG_ENABLED=false


# =========================================
# Set entrypoint
# =========================================
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN ["chmod", "+x", "/docker-entrypoint.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR $PROJECT_ROOT

CMD ["php-fpm", "-F"]
