FROM php:7.2

RUN apt-get update
RUN apt-get install -y gnupg2
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential
RUN apt-get install -y git libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libicu-dev g++ mysql-client
RUN docker-php-ext-install -j$(nproc) iconv intl zip mysqli
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd
RUN curl -o /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar
RUN chmod +x /usr/local/bin/phpunit
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

ENTRYPOINT ["docker-php-entrypoint"]

CMD ["php", "-a"]
