FROM php:7.1-apache

RUN apt-get update && apt-get install -y cron git-core jq vim \
  libjpeg-dev libpng-dev libpq-dev wget unzip && \
  rm -rf /var/lib/apt/lists/* && \
  docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
  docker-php-ext-install gd opcache zip mysqli pdo_mysql

RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=2'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/docker-oc-opcache.ini

RUN { \
    echo 'log_errors=on'; \
    echo 'display_errors=off'; \
    echo 'upload_max_filesize=32M'; \
    echo 'post_max_size=32M'; \
    echo 'memory_limit=128M'; \
  } > /usr/local/etc/php/conf.d/docker-oc-php.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
  /usr/local/bin/composer global require hirak/prestissimo

ENV COMPOSER_ALLOW_SUPERUSER=1

RUN a2enmod rewrite

RUN git clone https://github.com/JoeyChen-NTUT/advisory.yda.git --depth 1 . && \
  wget -O /usr/local/bin/docker-oc-entrypoint https://raw.githubusercontent.com/JoeyChen-NTUT/advisory.yda-docker/master/docker-oc-entrypoint && \
  composer install --no-interaction --prefer-dist --no-scripts && \
  composer clearcache && \
  git status && git reset --hard HEAD && git clean -f -d && \
  rm -rf .git && \
  find . -type d \( -path './plugins' -or  -path './storage' -or  -path './themes' -or  -path './plugins/*' -or  -path './storage/*' -or  -path './themes/*' \) -exec chmod g+ws {} \;

RUN echo "* * * * * /usr/local/bin/php /var/www/html/artisan schedule:run > /proc/1/fd/1 2>/proc/1/fd/2" > /etc/cron.d/october-cron && \
  crontab /etc/cron.d/october-cron

RUN echo 'exec php artisan "$@"' > /usr/local/bin/artisan && \
  echo 'exec php artisan tinker' > /usr/local/bin/tinker && \
  echo '[ $# -eq 0 ] && exec php artisan october || exec php artisan october:"$@"' > /usr/local/bin/october && \
  sed -i '1s;^;#!/bin/bash\n[ "$PWD" != "/var/www/html" ] \&\& echo " - Helper must be run from /var/www/html" \&\& exit 1\n;' /usr/local/bin/artisan /usr/local/bin/tinker /usr/local/bin/october && \
  chmod +x /usr/local/bin/artisan /usr/local/bin/tinker /usr/local/bin/october /usr/local/bin/docker-oc-entrypoint

ENTRYPOINT ["docker-oc-entrypoint"]
CMD ["apache2-foreground"]
