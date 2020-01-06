FROM cheezykins/laravel

MAINTAINER Rufus Mbugua - https://github.com/rufusmbugua

RUN echo "mysql-server-5.5 mysql-server/root_password password root" | debconf-set-selections \
    && echo "mysql-server-5.5 mysql-server/root_password_again password root" | debconf-set-selections \
    && apt-get update \
    && apt-get install --no-install-recommends -y mysql-server-5.5

ONBUILD RUN composer self-update \
        && cd /var/www/html \
        && composer update \
        --no-ansi \
        --no-dev \
        --no-interaction \
        --no-progress \
        --prefer-dist
WORKDIR /var/www/html
