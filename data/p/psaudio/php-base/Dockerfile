FROM psaudio/alpine-base

WORKDIR /usr/src

# create www-data user and group
RUN set -xe \
    && addgroup -g 82 -S www-data \
    && adduser -u 82 -D -S -G www-data www-data

# install packages needed by PHP during runtime
RUN set -xe \
    && apk add --update --no-cache --virtual .run-dependencies \
        libpng \
        libjpeg-turbo \
        freetype \
        libxml2-dev \
    && rm -rf /var/cache/apk/*

# build and install PHP
RUN set -xe \
    \
    # install packages needed to build PHP
    && apk add --update --no-cache --virtual .build-dependencies \
        autoconf \
        build-base \
        wget \
        dpkg-dev \
        dpkg \
    \
    # install packages needed to build GD
    && apk add --no-cache --virtual .gd-build-dependencies \
        libpng-dev \
        libjpeg-turbo-dev \
        freetype-dev \
    \
    # download and extract PHP source
    && wget -O php.tar.gz http://php.net/get/php-5.6.39.tar.gz/from/this/mirror \
    && tar -xzf php.tar.gz \
    \
    # configure PHP options
    && cd php-5.6.39/ \
    && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
    && ./configure \
        --build="$gnuArch" \
        # gd extension needed in powerdebug, burnin
        --with-gd \
        --with-freetype-dir=/usr/include/freetype2 \
        --with-jpeg-dir=/usr/include \
        # mysql extension used in powerdebug, burnin, rma
        --with-mysql \
        # mysqli extension used in labels
        --with-mysqli \
        --without-pdo-sqlite \
        --without-sqlite3 \
        --enable-mbstring \
        # zlib needed for FPDF library (rma, labels)
        --with-zlib \
        --enable-fpm \
        --with-fpm-user=www-data \
        --with-fpm-group=www-data \
        --with-config-file-path=/usr/local/etc/php \
        --with-config-file-scan-dir=/usr/local/etc/php/conf.d \
        --enable-option-checking=fatal \
    \
    # install PHP
    && make -j$(nproc) \
    && make install \
    \
    # create PHP configuration files
    && cp -v php.ini-development /usr/local/php/ \
    && mv -v /usr/local/etc/php-fpm.conf.default /usr/local/etc/php-fpm.conf \
    && cp -v sapi/fpm/php-fpm /usr/local/bin \
    \
    # compress PHP source
    && make clean \
    && cd /usr/src/ \
    && tar -cvz -f php.tar.gz php-5.6.39/ \
    \
    # cleanup
    && rm -rf /usr/src/php-5.6.39/ \
    && apk del .build-dependencies .gd-build-dependencies \
    && rm -rf /var/cache/apk/*

# install Xdebug
RUN set -xe \
    \
    # create directory for Xdebug output
    && mkdir -p /.xdebug/ \
    \
    # install build tools
    && apk add --no-cache --virtual .xdebug-build-dependencies \
        autoconf \
        build-base \
    \
    # install Xdebug
    && pecl install xdebug-2.5.5 \
    \
    # cleanup
    && apk del .xdebug-build-dependencies \
    && rm -rf /var/cache/apk/*

# configure PHP-FPM pools
RUN set -xe \
    \
    # log errors so we can see them with docker logs
    && sed -i 's!;error_log = log/php-fpm.log!error_log = /proc/self/fd/2!g' /usr/local/etc/php-fpm.conf \
    \
    # listen on port 9000 of all interfaces
    && sed -i 's!listen = 127.0.0.1:9000!listen = 9000!g' /usr/local/etc/php-fpm.conf \
    \
    # send pool worker output to fpm logs (configured above)
    && sed -i 's!;catch_workers_output!catch_workers_output!g' /usr/local/etc/php-fpm.conf \
    \
    # prevent concurrent file access to prevent errors in Docker for Windows (https://github.com/docker/for-win/issues/2005)
    && sed -i 's!pm = dynamic!pm = static!g' /usr/local/etc/php-fpm.conf \
    && sed -i 's!pm.max_children = 5!pm.max_children = 1!g' /usr/local/etc/php-fpm.conf \
    \
    # set the request timeout to prevent 504 errors when performing costly PHP operations
    && sed -i 's!;request_terminate_timeout!request_terminate_timeout!g' /usr/local/etc/php-fpm.conf
    # && sed -i 's!pm.max_spare_servers = 3!pm.max_spare_servers = 1!g' /usr/local/etc/php-fpm.conf \
    # && sed -i 's!pm.start_servers = 2!pm.start_servers = 1!g' /usr/local/etc/php-fpm.conf

WORKDIR /app/

CMD ["php-fpm", "-F"]

EXPOSE 9000