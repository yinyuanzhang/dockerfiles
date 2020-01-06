FROM ubuntu:trusty


RUN apt-get update && \
    apt-get install software-properties-common -y && \ 
    apt-get install -y language-pack-en-base && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --force-yes \
        pkg-config \
        wget \
        build-essential \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libgif-dev \
        libwebp-dev \
        nginx \
        php7.2 \
        php7.2-dev \
        php7.2-ldap \
        php7.2-imagick \
        php7.2-mysql \
        php7.2-curl \
        php7.2-mbstring \
        php7.2-tidy \
        php7.2-pgsql \
        php7.2-redis \
        php7.2-bcmath \
        php7.2-gd \
        php7.2-imap \
        php7.2-intl \
        php7.2-zip \
        php7.2-fpm \
        supervisor \
        zip \
        unzip \
        p7zip-full

RUN cd /tmp && \
    wget https://imagemagick.org/download/ImageMagick.tar.gz && \
    tar xvzf ImageMagick.tar.gz && \
    cd ImageMagick-* && \
    ./configure --with-webp && \
    make && \
    make install && \
    ldconfig /usr/local/lib

RUN cd /tmp && \
    wget https://pecl.php.net/get/imagick-3.4.3.tgz && \
    tar xvzf imagick-3.4.3.tgz && \
    cd imagick-* && \
    phpize && \
    ./configure && \
    make && \
    make install

#composer
RUN cd /var/tmp
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

#attach run folder
RUN mkdir /var/www
RUN mkdir /var/www/public
COPY index.php /var/www/public/index.php
COPY mime.types /etc/nginx/mime.types
COPY nginx.conf /etc/nginx/nginx.conf

VOLUME /var/www
VOLUME /etc/nginx/sites-enabled
VOLUME /etc/supervisor/conf.d

COPY entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
