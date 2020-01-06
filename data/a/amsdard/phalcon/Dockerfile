FROM amsdard/php:5

RUN curl -fsSL 'https://github.com/phalcon/cphalcon/archive/phalcon-v2.0.13.tar.gz' -o phalcon.tar.gz && \
    tar xvzf phalcon.tar.gz && cd cphalcon-*/build && ./install && cd ../.. && rm -rf phalcon && \
    docker-php-ext-enable phalcon

# ImageMagick
RUN curl -fsSL 'http://www.imagemagick.org/download/ImageMagick.tar.gz' -o ImageMagick.tar.gz && \
    tar xvzf ImageMagick.tar.gz && \
    cd ImageMagick-* && ./configure && make && make install && /sbin/ldconfig /usr/local/lib && \
    cd .. && rm -rf ImageMagick.tar.gz ImageMagick-* && \
    POLICY_XML_LOCATION="$(find /usr/local/etc/ -name 'policy.xml')" && \
    cp /files/imagemagick-policy.xml $POLICY_XML_LOCATION

RUN pecl install imagick xdebug-2.5.5 && \
    yes '' | pecl install -f redis && \
    docker-php-ext-enable imagick redis xdebug && \
    mkdir $PHP_INI_DIR/conf-available

ADD ./data/php-fpm-custom.sh /usr/local/bin/php-fpm-custom
ADD ./data/xdebug.ini $PHP_INI_DIR/conf-available/xdebug.ini

ENV RUN_AS_ROOT php-fpm-custom

CMD ["php-fpm-custom"]
