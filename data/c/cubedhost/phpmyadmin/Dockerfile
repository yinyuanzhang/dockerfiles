FROM phpmyadmin/phpmyadmin:latest
RUN apk add --no-cache --update --virtual buildDeps g++ libtool make autoconf && \
    pecl install redis && \
    docker-php-ext-enable redis && \
    apk del buildDeps autoconf g++ gcc libtool make
