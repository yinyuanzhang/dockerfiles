FROM php:7.2-fpm-alpine

# fix permissions
RUN { \
  sed -i'' 's/www-data:x:82:82:/www-data:x:1000:1000:/g' /etc/passwd; \
  mkdir -p /usr/local/var/run/php; \
  echo 'listen = /usr/local/var/run/php/www.sock' >> /usr/local/etc/php-fpm.d/zz-docker.conf; \
}

WORKDIR /usr/src/php/ext/

#zip
RUN apk --no-cache add zlib-dev \
  && docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) zip

#pdo
RUN docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) pdo

#mysql
RUN docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) pdo_mysql mysqli

#sqlite
RUN apk add --no-cache --virtual=.build-dependencies sqlite-dev \
  && docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) pdo_sqlite \
  && apk del --no-cache .build-dependencies

#gd
RUN \
        apk add --no-cache freetype libjpeg-turbo libpng && \
        apk add --no-cache --virtual=.build-dependencies freetype-dev libjpeg-turbo-dev libpng-dev && \
        docker-php-ext-configure gd \
                --enable-gd-native-ttf \
                --with-freetype-dir=/usr/include/ \
                --with-jpeg-dir=/usr/include/ \
                --with-png-dir=/usr/include/ && \
        docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd && \
        apk del --no-cache .build-dependencies

#soap
RUN \
        apk add --no-cache --virtual=.build-dependencies libxml2-dev && \
        docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) soap && \
        apk del --no-cache .build-dependencies

#imagick
#RUN apk add --no-cache --virtual=.build-dependencies imagemagick-dev && \
#  docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) imagick && \
#  apk del --no-cache .build-dependencies
RUN \
        apk add --no-cache --virtual=.build-dependencies autoconf gcc g++ imagemagick-dev libtool make $PHPIZE_DEPS && \
        apk add --update imagemagick-dev && \
        pecl install imagick && \
        docker-php-ext-enable imagick && \
        apk del --no-cache .build-dependencies

#Phalcon
ENV PHALCON_VERSION=3.3.1
RUN \
        curl -L https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz -o archive.tar.gz && \
        mkdir -p phalcon && \
        tar xzf archive.tar.gz -C phalcon --strip-components=1 && \
        rm archive.tar.gz && \
        apk add --no-cache --virtual=.build-dependencies $PHPIZE_DEPS && \
        cd phalcon/build && \
        sh install && \
        echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/docker-php-ext-phalcon.ini && \
        apk del --no-cache .build-dependencies

#Igbinary
ENV IGBINARY_VERSION=2.0.5
RUN \
        curl -L https://github.com/igbinary/igbinary/archive/${IGBINARY_VERSION}.tar.gz -o archive.tar.gz && \
        mkdir -p igbinary && \
        tar xzf archive.tar.gz -C igbinary --strip-components=1 && \
        rm archive.tar.gz && \
        apk add --no-cache --virtual=.build-dependencies $PHPIZE_DEPS && \
        docker-php-ext-configure igbinary \
                CFLAGS="-O2 -g" \
                --enable-igbinary && \
        docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) igbinary && \
        echo "session.serialize_handler=igbinary" >> /usr/local/etc/php/conf.d/docker-php-ext-igbinary.ini && \
        apk del --no-cache .build-dependencies

#Redis
ENV PHPREDIS_VERSION=4.0.0RC1
RUN \
        curl -L https://github.com/phpredis/phpredis/archive/${PHPREDIS_VERSION}.tar.gz -o archive.tar.gz && \
        mkdir -p phpredis && \
        tar xzf archive.tar.gz -C phpredis --strip-components=1 && \
        rm archive.tar.gz && \
        apk add --no-cache --virtual=.build-dependencies $PHPIZE_DEPS && \
        docker-php-ext-configure phpredis \
                --enable-redis-igbinary && \
        docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) phpredis && \
        apk del --no-cache .build-dependencies

#Compile XDebug
ENV XDEBUG_VERSION=2.6.0
RUN \
        curl -L https://github.com/xdebug/xdebug/archive/${XDEBUG_VERSION}.tar.gz -o archive.tar.gz && \
        echo curl -L https://github.com/xdebug/xdebug/archive/${XDEBUG_VERSION}.tar.gz -o archive.tar.gz && \
        mkdir -p xdebug && \
        tar xvf archive.tar.gz -C xdebug --strip-components=1 && \
        rm archive.tar.gz && \
        apk add --no-cache --virtual=.build-dependencies $PHPIZE_DEPS && \
        docker-php-ext-configure xdebug \
                --enable-xdebug && \
        docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) xdebug && \
        apk del --no-cache .build-dependencies

#Compile gmp
RUN \
        apk add --no-cache --virtual=.build-dependencies $PHPIZE_DEPS gmp-dev && \
        docker-php-ext-install gmp && \
        apk del --no-cache .build-dependencies

#Compile WKHTMLTOPDF
#ENV WKHTMLTOPDF_VERSION=1.0.0
#RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
#RUN \
#       curl -L https://github.com/Saoneth/php-wkhtmltox/archive/${WKHTMLTOPDF_VERSION}.tar.gz -o archive.tar.gz && \
#       mkdir -p wkhtmltopdf && \
#       tar xzf archive.tar.gz -C wkhtmltopdf --strip-components=1 && \
#       rm archive.tar.gz && \
#       apk add --no-cache wkhtmltopdf && \
#       apk add --no-cache --virtual=.build-dependencies wkhtmltopdf-dev $PHPIZE_DEPS && \
#       ls -l /usr/lib/libwkhtmltox* /usr/include/wkhtmltox/ && \
#       cat /usr/include/wkhtmltox/pdf.h && \
#       docker-php-ext-configure wkhtmltopdf && \
#       docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) wkhtmltopdf && \
#       apk del --no-cache .build-dependencies
