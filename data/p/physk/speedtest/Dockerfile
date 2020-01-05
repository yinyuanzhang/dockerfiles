FROM php:7.1-apache
EXPOSE 80
WORKDIR /var/www/html/
COPY . /var/www/html
RUN chown -hR www-data:www-data /var/www/html \
    && ln -s /var/www/html /var/www/html/speedtest \
    && apt update \
    && apt install -y libpng-dev \
                    libwebp-dev \
                    libjpeg62-turbo-dev \
                    libpng-dev libxpm-dev \
                    libfreetype6-dev \
                    libmcrypt-dev \
    && docker-php-ext-configure gd \
                    --with-gd \
                    --with-webp-dir \
                    --with-jpeg-dir \
                    --with-png-dir \
                    --with-zlib-dir \
                    --with-xpm-dir \
                    --with-freetype-dir \
                    --enable-gd-native-ttf \
    && docker-php-ext-install gd \
    && docker-php-ext-install mcrypt

CMD ["/usr/local/bin/apache2-foreground"]