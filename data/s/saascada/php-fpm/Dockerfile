# Image Located: Dockerhub - saascada/php-fpm
# Build: docker build -t saascada/php-fpm .
# Push: docker push saascada/php-fpm
FROM php:7.3-fpm-alpine

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

RUN apk add libxslt-dev gmp-dev
RUN docker-php-ext-install gmp
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install xsl
RUN docker-php-ext-install fileinfo
