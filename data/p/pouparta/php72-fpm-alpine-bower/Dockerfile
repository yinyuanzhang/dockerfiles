FROM php:7.2-fpm-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache \
    bash \
    openssh \
    zip \
    jpegoptim optipng pngquant gifsicle \
    mysql-client \
    freetype-dev \
    libjpeg-turbo-dev \
    libpng-dev
    #\
    #gettext

# Install Git
RUN apk add --update --no-cache git

# Install APCU
# Ref: https://github.com/m2sh/php7/blob/master/alpine/Dockerfile
RUN docker-php-source extract \
    && apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \
    && pecl install apcu \
    && docker-php-ext-enable apcu \
    && apk del .phpize-deps-configure \
    && docker-php-source delete

# Configure locales
# Ref1: https://github.com/sgerrand/alpine-pkg-glibc
# Ref2: https://gist.github.com/Herz3h/0ffc2198cb63949a20ef61c1d2086cc0
# Note that locale -a is not available in alpine linux, use `/usr/glibc-compat/bin/locale -a` instead
RUN apk --no-cache add ca-certificates wget && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-bin-2.29-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-i18n-2.29-r0.apk && \
    apk add glibc-bin-2.29-r0.apk glibc-i18n-2.29-r0.apk glibc-2.29-r0.apk
RUN /usr/glibc-compat/bin/localedef -i en_CA -f UTF-8 en_CA.UTF-8
RUN /usr/glibc-compat/bin/localedef -i fr_CA -f UTF-8 fr_CA.UTF-8

# Install language pack
# Source: https://wiki.alpinelinux.org/wiki/Setting_the_timezone
RUN apk add --no-cache tzdata
RUN ln -sf /usr/share/zoneinfo/America/Toronto /etc/localtime
RUN echo "America/Toronto" >  /etc/timezone
ENV TZ America/Toronto
ENV LANG en_CA.UTF-8
ENV LANGUAGE en_CA.UTF-8
ENV LC_ALL en_CA.UTF-8

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring zip exif pcntl
RUN docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd
#RUN docker-php-ext-configure gettext --with-gettext=/usr/glibc-compat/bin/locale
#RUN docker-php-ext-install gettext

## NodeJS, NPM
# Install NodeJS
RUN apk add --no-cache --update nodejs nodejs-npm

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer


# Install Bower globally
RUN npm install -g bower

# Set the build place
WORKDIR /var/www/html
