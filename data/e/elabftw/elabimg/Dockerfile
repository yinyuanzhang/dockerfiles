# elabftw + nginx + php-fpm in a container
FROM alpine:3.10

# select version or branch here
ENV ELABFTW_VERSION dev

# this is versioning for the container image
ENV ELABIMG_VERSION 1.4.0

LABEL org.label-schema.name="elabftw" \
    org.label-schema.description="Run nginx and php-fpm to serve elabftw" \
    org.label-schema.url="https://www.elabftw.net" \
    org.label-schema.vcs-url="https://github.com/elabftw/elabimg" \
    org.label-schema.version=$ELABFTW_VERSION \
    org.label-schema.maintainer="nicolas.carpi@curie.fr" \
    org.label-schema.schema-version="1.0"

# install nginx and php-fpm
# php7-gd is required by mpdf for transparent png
# php7-tokenizer and php7-xmlwriter are for dev only
# don't put line comments inside this instruction
RUN apk upgrade -U -a && apk add --no-cache \
    autoconf \
    bash \
    build-base \
    coreutils \
    curl \
    freetype \
    ghostscript \
    git \
    graphicsmagick-dev \
    openssl \
    libtool \
    nginx \
    openjdk8-jre \
    php7 \
    php7-curl \
    php7-ctype \
    php7-dev \
    php7-dom \
    php7-exif \
    php7-gd \
    php7-gettext \
    php7-fileinfo \
    php7-fpm \
    php7-json \
    php7-mbstring \
    php7-opcache \
    php7-openssl \
    php7-pdo_mysql \
    php7-pear \
    php7-phar \
    php7-redis \
    php7-session \
    php7-tokenizer \
    php7-xmlwriter \
    php7-zip \
    php7-zlib \
    tzdata \
    unzip \
    yarn \
    supervisor && \
    pecl install gmagick-2.0.5RC1 && echo "extension=gmagick.so" >> /etc/php7/php.ini && \
    apk del autoconf build-base libtool php7-dev

WORKDIR /elabftw

# install composer
RUN echo "$(curl -sS https://composer.github.io/installer.sig) -" > composer-setup.php.sig \
    && curl -sS https://getcomposer.org/installer | tee composer-setup.php | sha384sum -c composer-setup.php.sig \
    && php composer-setup.php && rm composer-setup.php*

# for dev only, copy composer in $PATH
RUN cp /elabftw/composer.phar /usr/bin/composer

# nginx will run on port 443
EXPOSE 443

# copy configuration and run script
COPY ./src/nginx/ /etc/nginx/
COPY ./src/supervisord.conf /etc/supervisord.conf
COPY ./src/run.sh /run.sh

# remove this file because it's useless and causes issues when doing composer upgrade
RUN rm -f /.dockerenv

# start
CMD ["/run.sh"]

# define mountable directories
VOLUME /elabftw
VOLUME /ssl
