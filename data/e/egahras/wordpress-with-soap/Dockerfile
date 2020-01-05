FROM wordpress
RUN apt-get update && \
    apt-get install -y libxml2-dev && \
    docker-php-ext-install soap && \
    pecl install xdebug-2.6.1 && \
    docker-php-ext-enable xdebug