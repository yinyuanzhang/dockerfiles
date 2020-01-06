FROM php:7-fpm
 RUN apt-get update && apt-get install -y \
    vim \
    zip \
    unzip \
    zlib1g-dev \
    iputils-ping \
    git
 RUN docker-php-ext-install \
    pdo_mysql mysqli \
    zip 
 RUN curl -s http://getcomposer.org/installer | php && \
    echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \
    mv composer.phar /usr/local/bin/composer 
 RUN composer global require "laravel/installer=~1.1" && \
    echo "export PATH=~/.composer/vendor/bin:$PATH" >> ~/.bashrc
 RUN bash -c "source ~/.bashrc"
