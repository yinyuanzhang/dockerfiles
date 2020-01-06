FROM webdevops/php-nginx-dev:7.3

ARG ZEPHIR_VERSION=0.12.2
ARG PHALCON_VERSION=3.4.4
ARG EXT_FOLDER=/usr/local/lib/php/extensions/no-debug-non-zts-20180731/

# Switch to root user
USER root

# Install zephir compiler
RUN set -x && \
    git clone git://github.com/phalcon/php-zephir-parser.git && \
    cd php-zephir-parser && \
    phpize && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf php-zephir-parser && \
    echo "extension=zephir_parser.so" > /usr/local/etc/php/conf.d/99-phalcon.ini

# Install cphalcon
RUN set -x && \
    git clone https://github.com/phalcon/cphalcon && \
    cd cphalcon && \
    wget https://github.com/phalcon/zephir/releases/download/${ZEPHIR_VERSION}/zephir.phar && \
    git checkout tags/v${PHALCON_VERSION} && \
    php zephir.phar fullclean && \
    php zephir.phar build && \
    cp ext/modules/phalcon.so ${EXT_FOLDER} && \
    cd .. && \
    rm -rf cphalcon && \
    echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/99-phalcon.ini && \
    rm -rf ${EXT_FOLDER}/zephir_parser.so

# Configuring nginx to be compatible with phalcon
COPY nginx/conf.d/phalcon.conf /opt/docker/etc/nginx/vhost.common.d/
RUN rm /opt/docker/etc/nginx/vhost.common.d/10-php.conf
RUN rm /opt/docker/etc/nginx/vhost.common.d/10-location-root.conf

RUN set -x && \
    apt-get update && \
    apt-get install -y libyaml-dev libgmp-dev && \
    pecl install yaml && \
    echo "extension=yaml.so" > /usr/local/etc/php/conf.d/99-yaml.ini && \
    docker-php-ext-install gmp

# Switch again to application user
USER application
