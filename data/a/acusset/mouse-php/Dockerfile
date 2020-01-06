FROM php:7.1-fpm

ARG user_id
ARG group_id


RUN apt-get update && \
    apt-get install -y \
    git \
    zip \
    unzip \
    libmcrypt-dev \
    libmagickwand-dev \
    libicu-dev

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

ENV COMPOSER_ALLOW_SUPERUSER 1

RUN docker-php-ext-install pdo pdo_mysql mbstring mcrypt intl zip

# Add User
RUN id -u "$user_id" &>/dev/null || (useradd -u "$user_id" -g "$group_id" -m dev && \
  mkdir /home/dev/.composer && \
  chown dev /home/dev/.composer && \
  mkdir -p /home/dev/.ssh && \
  chown dev /home/dev/.ssh)

COPY php.ini /usr/local/etc/php/php.ini

RUN pecl install apcu \
  && docker-php-ext-enable apcu

RUN pecl install imagick \
  && docker-php-ext-enable imagick

RUN docker-php-ext-install opcache
