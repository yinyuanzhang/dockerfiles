FROM eboost/php7fpm

RUN docker-php-ext-install zip

# Install modules
RUN apt-get update && apt-get install -y git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

CMD ["composer"]
