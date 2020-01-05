# Keep update latest PHP official image by specific minor version for newer builds
FROM php:7.2.21-apache-stretch

# System dependencies
RUN apt-get update && apt-get install -y \
        gettext \
        git \
        gosu \
        libfreetype6 \
        libfreetype6-dev \
        libjpeg62 \
        libjpeg62-turbo-dev \
        libpng-dev \
        locales \
        ssh-client \
        unzip \
        wget \
        zlib1g-dev \
    --no-install-recommends \
    && rm -r /var/lib/apt/lists/*


# Extensions
RUN docker-php-ext-install -j$(nproc) zip mysqli pdo_mysql
RUN ["/bin/bash", "-c", "docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/"]
RUN docker-php-ext-install -j$(nproc) gd

# Install PHP extensions
RUN a2enmod rewrite && a2enmod headers

# Composer
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer -O - -q | php -- --quiet
RUN chmod +x composer.phar
RUN mv composer.phar /usr/local/bin/composer

RUN set -e \
    && composer global require hirak/prestissimo \
    && composer clear-cache

# Set workspace & extended INI for flexible config (eg. file upload limit)
COPY . /data
WORKDIR /data

COPY extended.php.ini /usr/local/etc/php/conf.d/extended.php.ini


# Change base backend port to 8080 to avoid privilege ports when running user is not root
RUN sed -i 's/Listen\ 80/Listen\ 8080/g' /etc/apache2/ports.conf
RUN sed -i 's/\*\:80/\*\:8080/g' /etc/apache2/sites-enabled/000-default.conf
RUN sed -i 's/\/var\/www\/html/\/data\/public\n<Directory \/data\/public>\nAllowOverride All\nRequire all granted\n<\/Directory>\nServerName example.com/g' \
    /etc/apache2/sites-enabled/000-default.conf

EXPOSE 8080


# Generate various dummy users (app1 ~ appN) for buffer some host user uids
RUN for i in `seq 1 5`; do useradd -M -s /bin/false app$i; done

# Extend this image for additional libraries (eg. wkhtmltopdf, imagemagick, mcrypt, etc.)
