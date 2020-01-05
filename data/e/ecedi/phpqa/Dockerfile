FROM php:7.2-alpine

RUN wget -O composer.phar https://getcomposer.org/download/1.9.0/composer.phar \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer

ENV COMPOSER_MEMORY_LIMIT=-1

RUN apk add --no-cache git

RUN composer global require drupal/coder
RUN composer global require dealerdirect/phpcodesniffer-composer-installer

RUN apk add --no-cache libxslt-dev \
    && docker-php-ext-configure xsl \
    && docker-php-ext-install -j$(nproc) xsl

RUN composer global require edgedesign/phpqa --update-no-dev

ENV PATH="/root/.composer/vendor/bin/:${PATH}" 
