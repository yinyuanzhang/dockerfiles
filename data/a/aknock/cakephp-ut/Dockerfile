FROM php:5.5
# Install modules
RUN apt-get update && apt-get install -y \
        libicu-dev libicu-dev zlib1g-dev git wget mysql-client lftp ruby ruby-dev
RUN gem install sass
RUN docker-php-ext-install intl mbstring zip mysql mysqli pdo_mysql pdo
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
CMD ["php"]
