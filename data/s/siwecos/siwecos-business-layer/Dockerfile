FROM php:7.2-apache

# Settings
ENV PYTHON_VERSION=2.7.13-r1
ENV PY_PIP_VERSION=9.0.1-r1
ENV SUPERVISOR_VERSION=3.3.3
ENV APP_HOME /var/www/html

ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8

# Install all dependencies and generate the locales
RUN apt-get update -y \
    && apt-get install -y openssl vim zip unzip git libpng-dev zlib1g-dev python python-pip locales \
    && sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && docker-php-ext-install mysqli pdo_mysql pdo mbstring gd zip \
    && pip install supervisor==$SUPERVISOR_VERSION \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

# Copy configuration files
COPY php.ini /usr/local/etc/php/
COPY worker.conf /etc/supervisor/supervisord.conf

# Change uid and gid of apache to docker user uid/gid
# Change the web_root to laravel /var/www/html/public folder
# Enable apache module rewrite
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data \
    && sed -i -e "s/html/html\/public/g" /etc/apache2/sites-enabled/000-default.conf \
    && a2enmod rewrite

# Copy source files and run composer
WORKDIR /var/www/html

COPY . $APP_HOME
COPY .env.example .env

# Install all PHP dependencies and change ownership of our applications
RUN composer install --no-interaction \
    && chown -R www-data:www-data $APP_HOME

CMD supervisord --nodaemon --configuration /etc/supervisor/supervisord.conf

EXPOSE 80
