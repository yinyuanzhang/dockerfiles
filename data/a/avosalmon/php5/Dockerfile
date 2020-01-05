FROM php:5.6.36-fpm
LABEL author="Ryuta Hamasaki"

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV LC_CTYPE C.UTF-8

RUN apt-get update && apt-get install -y \
        curl \
        gnupg2 \
        git \
        procps \
        ffmpeg \
        tmux \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install zip \
    && docker-php-ext-install bcmath \
    && rm -rf /var/lib/apt/lists/*

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer \
    && chmod 755 /usr/local/bin/composer

# Add www-data to root group, so that it has write permissions to storage/framework/views
RUN usermod -a -G root www-data

# Other shell scripts
RUN echo '#!/bin/bash\nls -lah "$@"' > /usr/local/bin/ll \
    && chmod 755 /usr/local/bin/ll

CMD ["php-fpm"]
